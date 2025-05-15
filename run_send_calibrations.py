import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calibra_tech.settings')
django.setup()

from notificaciones.utils import enviar_calibraciones_del_mes

if __name__ == '__main__':
    enviar_calibraciones_del_mes()