from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

ALLOWED_HOSTS = ['.bidici.com']
ALLOW_ORIGIN = "http://bidici.com"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['BIDICI_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['BIDICI_DB_NAME'],
        'USER': os.environ['BIDICI_DB_USER'],
        'PASSWORD': os.environ['BIDICI_DB_PASS'],
        'HOST': os.environ['BIDICI_DB_HOST'],
        'PORT': os.environ['BIDICI_DB_PORT'],
    }
}
