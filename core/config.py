import os

from starlette.config import Config

config = Config('.env_dev')

url = os.environ.get('DATABASE_URL')
url = url.split('//')[1]
DATABASE_URL = f'postresql://{url}'
# DATABASE_URL = config('EE_DATABASE_URL', cast=str, default='')

SECRET_KEY = os.environ.get('SECRET_KEY')
# SECRET_KEY = 'bc52a97330b499365abaf1716ffc70c7

ALGORITM = 'HS256'

ACCESS_TOKEN_EXPIRE_MINUTES = 60
