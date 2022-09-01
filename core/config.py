import os

from starlette.config import Config

config = Config('.env_dev')


# DATABASE_URL = os.environ.get('DB_URL')
DATABASE_URL = config('EE_DATABASE_URL', cast=str, default='')

SECRET_KEY = config('EE_DATABASE_URL', cast=str, default='bc52a97330b499365abaf1716ffc70c7')

ALGORITM = 'HS256'

ACCESS_TOKEN_EXPIRE_MINUTES = 60
