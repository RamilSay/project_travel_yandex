import os

from dotenv import load_dotenv
from typing import Literal

load_dotenv()

EnvType = Literal['local', 'remote']
ENVIRONMENT: EnvType = 'local'

USER_LOGIN = os.getenv('login')
USER_PASSWORD = os.getenv('password')

SELENOID_LOGIN = os.getenv('selenoid_login')
SELENOID_PASSWORD = os.getenv('selenoid_password')



