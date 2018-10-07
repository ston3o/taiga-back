from .common import *

PUBLIC_REGISTER_ENABLED = False
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = '$TAIGA_SECRET'

MEDIA_URL = "$SCHEME://$TAIGA_HOST/media/"
STATIC_URL = "$SCHEME://$TAIGA_HOST/static/"
ADMIN_MEDIA_PREFIX = "$SCHEME://$TAIGA_HOST/static/admin/"
SITES["api"]["scheme"] = "$SCHEME"
SITES["api"]["domain"] = "$TAIGA_HOST"
SITES["front"]["scheme"] = "$SCHEME"
SITES["front"]["domain"] = "$TAIGA_HOST"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "$DB_NAME",
        "HOST": "$DB_HOST",
        "USER": "$DB_USER",
        "PASSWORD": "$DB_PASSWORD"
    }
}

#DEFAULT_FROM_EMAIL = "john@doe.com"
#CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = False # You cannot use both (TLS and SSL) at the same time!
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'user'
#EMAIL_HOST_PASSWORD = 'password'

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://$RABBIT_USER:$RABBIT_PASSWORD@$RABBIT_HOST:$RABBIT_PORT/$RABBIT_VHOST"}