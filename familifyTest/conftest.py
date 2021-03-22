import pytest
import sys
import os
ruta = os.path.realpath(os.path.join(os.path.dirname(__file__),'../../..'))
sys.path.append(ruta)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'familifyTest.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    if settings.DEBUG:
        settings.DATABASES['default'] = settings.DATABASES['default']
    else:
        pass

@pytest.fixture(autouse=True)
def enable_db_access_for_all_test(db):
    pass