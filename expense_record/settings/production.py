from .base import *  # noqa
from decouple import config

DEBUG = False

SERVER = config("SERVER", default="")

ALLOWED_HOSTS.append(SERVER)
