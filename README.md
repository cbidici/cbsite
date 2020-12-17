# cbsite

Backend for personal web-site.

## Run

### Environment

#### Local
1. `pip install -r requirements\local.txt`
2. `python manage.py makemigrations --settings cbsite.settings.local`
3. `python manage.py migrate --settings cbsite.settings.local`
4. `python manage.py runserver --settings cbsite.settings.local`

### Create Super User
`python manage.py createsuperuser --settings cbsite.settings.local`
