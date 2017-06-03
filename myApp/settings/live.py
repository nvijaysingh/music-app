from myApp.settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'musicappdatabase',
        'USER': 'musicapp',
        'PASSWORD': 'nvijaysingh',
        'HOST': 'nvijaysingh2.cttpvqsadktu.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
