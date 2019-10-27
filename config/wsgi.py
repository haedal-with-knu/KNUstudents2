"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# apache config
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('~/KNUstudents2/config')

application = get_wsgi_application()
