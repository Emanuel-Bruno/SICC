import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'sistema_sicc.settings.base'
django.setup()