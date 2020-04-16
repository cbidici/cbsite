from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

ALLOWED_HOSTS = []
ALLOW_ORIGIN = "http://127.0.0.1:3000"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '846^vig%ubw6othjw_d%6@983@e-2_xnrwe&932$0l&n5nr^8#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}
