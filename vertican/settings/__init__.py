import os
from decouple import config

if os.environ.get('ENVIRONMENT') == 'production':
    from vertican.settings.prod_settings import *
elif os.environ.get('ENVIRONMENT') == 'development':
    from vertican.settings.dev_settings import *
