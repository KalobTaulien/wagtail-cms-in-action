from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-j(68f)@#93jw$hpoe2)(ndzes8dlqo3^^89)2##l%x*+dc!%l%"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS = INSTALLED_APPS + [
    'django_extensions',
]

try:
    from .local import *
except ImportError:
    pass
