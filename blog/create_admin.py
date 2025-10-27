import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
email = 'admin@example.com'
password = 'admin@123'  # Change this to a strong password!

try:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"✅ Superuser '{username}' created successfully!")
    else:
        print(f"ℹ️ Superuser '{username}' already exists.")
except Exception as e:
    print(f"❌ Error creating superuser: {e}")