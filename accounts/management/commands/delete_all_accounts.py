from django.core.management.base import BaseCommand

from accounts.models import User

# python manage.py delete_all_accounts - DELETE ALL ACCOUNTS FROM DB


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
