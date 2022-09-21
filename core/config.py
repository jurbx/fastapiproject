import os

from starlette.config import Config

config = Config('.env_dev')

url = 'postgres://jgwcmktftfxhxz:fa471ac99fab8beb811a24598a5f4a101a1993f680d698f4921d18ea3960e18f@ec2-34-241-90-235.eu-west-1.compute.amazonaws.com:5432/d9dnvpsak351rc'
url = url.split('//')[1]
DATABASE_URL = f'postresql://{url}'
# DATABASE_URL = config('EE_DATABASE_URL', cast=str, default='')

SECRET_KEY = os.environ.get('SECRET_KEY')
# SECRET_KEY = 'bc52a97330b499365abaf1716ffc70c7

ALGORITM = 'HS256'

ACCESS_TOKEN_EXPIRE_MINUTES = 60
