from random   import choice
from string   import ascii_letters, digits

SECRET_KEY = ''.join([choice(ascii_letters + digits) for n in range(64)])

DEBUG = False

ALLOWED_HOSTS = ['webapp-180930.pythonanywhere.com',
                 'www.minaw.net']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'leminaw$names',
        'USER': 'leminaw',
        'PASSWORD': 'connectDB',
        'HOST': 'leminaw.mysql.pythonanywhere-services.com'
    }
}