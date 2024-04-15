from pydantic_settings import BaseSettings
from typing import Literal


class Config(BaseSettings):
    browser_version: str = ''
    base_url: str = 'https://travel.yandex.ru/'
    envtype: Literal['local', 'remote'] = 'local'
    driver_remote_url: str = ''




