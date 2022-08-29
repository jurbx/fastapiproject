from starlette.config import Config
import os


DATABASE_URL = os.environ.get('DB_URL')

SECRET_KEY = config('SECRET_KEY', cast=str, default='bc52a97330b499365abaf1716ffc70c7')

ALGORITM = 'HS256'

ACCESS_TOKEN_EXPIRE_MINUTES = 60
