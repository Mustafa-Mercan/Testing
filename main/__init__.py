from .settings.base import *

ENV_NAME = config("ENV_NAME")

if ENV_NAME == 'DEV':
    from .settings.dev import *
elif ENV_NAME == 'PROD':
    from .settings.prod import *