from pydantic_settings import BaseSettings
from typing import Literal


class Config(BaseSettings):
    selenoid_login: str = ''
    selenoid_password: str = ''
    browser_version: str = ''
    test_site_lang: str = 'ru'
    base_url: str = 'https://travel.yandex.ru/'
    envtype: Literal['local', 'remote'] = 'local'
    driver_remote_url: str = ''




