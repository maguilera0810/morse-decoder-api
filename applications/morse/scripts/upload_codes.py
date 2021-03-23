import sys
import os
ruta = os.path.realpath(os.path.join(os.path.dirname(__file__),'../../..'))
sys.path.append(ruta)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'familifyTest.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from applications.morse.models import CodigoMorse


def read_files(name_file='codes.txt'):
    with open(name_file, 'r') as file:
        for line in file:
            line = line.rstrip('\n').split(',')
            try:
                cod = CodigoMorse(character=line[0], code=line[1])
                cod.save()
            except Exception as e:
                print('ERROR--> ', e)

if __name__ == '__main__':
    read_files()
