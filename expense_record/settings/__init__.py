from .base import *  # noqa
from decouple import config

ENV_NAME = config("ENV_NAME", default="")

if ENV_NAME == "Development" or ENV_NAME == "":
    from .development import *  # noqa
elif ENV_NAME == "Production":
    from .production import *  # noqa
else:
    raise Exception("ENV_NAME env var is invalid")
