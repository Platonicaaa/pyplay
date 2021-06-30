"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from encrypted_secrets import load_secrets, YAMLFormatException

try:
    load_secrets()
except YAMLFormatException:
    print("\n\n\nMALFORMED YAML IN ENCRYPTED SECRETS\n\n\n")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
