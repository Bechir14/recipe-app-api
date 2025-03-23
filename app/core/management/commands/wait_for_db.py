#django command to wait for the db

import time 

from psycopg2 import OperationalError as psycopg2OpError
from django.db.utils import OperationalError


from django.core.management.base import BaseCommand



class Command(BaseCommand):
    def handle(self, *args, **options):
        """entry point for the command """

        self.stdout.write('waiting for database ')
        db_up = False

        while db_up is False :
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2OpError , OperationalError):
                self.stdout.write('Database unavailable waiting 2 seconds....')
                time.sleep(2) 

        self.stdout.write(self.style.SUCCESS("Database available"))

        