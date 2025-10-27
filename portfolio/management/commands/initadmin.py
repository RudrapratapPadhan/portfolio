from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Creates or updates superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not password:
            self.stdout.write(
                self.style.WARNING('No DJANGO_SUPERUSER_PASSWORD set. Skipping.')
            )
            return

        try:
            # Get or create user
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'is_staff': True,
                    'is_superuser': True,
                }
            )
            
            # Always update password (in case it changed)
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.email = email
            user.save()
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Superuser "{username}" created!')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Superuser "{username}" password updated!')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error: {e}')
            )