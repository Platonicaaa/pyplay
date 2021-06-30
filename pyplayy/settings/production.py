from .base import *
import django_heroku

DEBUG = False

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True

# Activate Django-Heroku.
django_heroku.settings(locals())
