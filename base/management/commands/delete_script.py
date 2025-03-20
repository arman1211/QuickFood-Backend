from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    help = "Delete all User records"

    def handle(self, *args, **kwargs):
        count, _ = CustomUser.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"✅ Successfully deleted {count}  records."))
