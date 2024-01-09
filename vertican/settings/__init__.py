import os
from decouple import config

if config('ENVIRONMENT') == 'production':
    from vertican.settings.prod_settings import *
elif config('ENVIRONMENT') == 'development':
    from vertican.settings.dev_settings import *
