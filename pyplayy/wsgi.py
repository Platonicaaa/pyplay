"""
WSGI config for pyplayy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application
from encrypted_secrets import load_secrets, YAMLFormatException

# Load encrypted secrets
try:
    load_secrets()
except YAMLFormatException:
    print("\n\n\nMALFORMED YAML IN ENCRYPTED SECRETS\n\n\n")

# Load environment specific variables
dotenv.load_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyplayy.settings.development')
if os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')

application = get_wsgi_application()
