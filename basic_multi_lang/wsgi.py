"""
WSGI config for basic_multi_lang project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

#activate_this = "/home/phaniv/nirbhay/virtual_evn/tes/bin/activate_this.py"
#execfile(activate_this, dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basic_multi_lang.settings")

application = get_wsgi_application()
