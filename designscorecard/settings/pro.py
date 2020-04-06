from .base import *

DEBUG = False

if not DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST_USER = "username"
    EMAIL_HOST = 'smtp.domain.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = "password"
else:
    EMAIL_BACKEND = (
        "django.core.mail.backends.console.EmailBackend"
    )


    ALLOWED_HOSTS = []

ADMINS = (
    ('Noah Olatoye', 'noaholatoye101@gmail.com'),
    ('Kevwe Kuale', 'kaykuale@gmail.com'),
    ('Noah Olatoye', 'nolatoye@instincthub.com'),
)
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
    }
}
