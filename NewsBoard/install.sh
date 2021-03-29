python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser(username='$SUPERUSER_NAME', password='$SUPERUSER_PASSWORD')" | python manage.py shell
python manage.py collectstatic
