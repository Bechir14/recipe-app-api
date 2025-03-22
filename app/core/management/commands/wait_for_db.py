#django command to wait for the db




from django.core.management.base import BaseCommand



class Command(BaseCommand):
    def handle(self, *args, **options):
        pass