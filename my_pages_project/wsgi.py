"""
WSGI config for my_pages_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_pages_project.settings')

application = get_wsgi_application()

# /home/art/git/DFB38_03_mypages_app/my_pages_project/wsgi.py