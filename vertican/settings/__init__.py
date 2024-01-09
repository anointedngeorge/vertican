import os
from decouple import config

if os.environ['ENVIRONMENT'] == 'production':
    from vertican.settings.prod_settings import *
elif os.environ['ENVIRONMENT'] == 'development':
    from vertican.settings.dev_settings import *
