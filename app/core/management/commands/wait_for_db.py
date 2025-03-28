# Django command to wait for the database

import time
from psycopg2 import OperationalError as psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database to be available."""

    def handle(self, *args, **options):
        """Entry point for the command."""

        self.stdout.write("Waiting for database...")
        db_up = False

        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 2 seconds...")
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS("Database available!"))
# noqa