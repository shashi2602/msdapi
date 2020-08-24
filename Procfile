release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input


web: gunicorn msd.wsgi --log-file -