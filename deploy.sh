source $VENV/bin/activate
export DJANGO_SETTINGS_MODULE=django_template.settings.production
git pull
pip install -r requirements.txt

# Update database, static files, locales
manage.py syncdb  --noinput
manage.py migrate
manage.py collectstatic --noinput
manage.py makemessages -a
manage.py compilemessages

# restart wsgi
touch project_name/wsgi.py
