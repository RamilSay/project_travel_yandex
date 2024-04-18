from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    base_url: str = 'https://travel.yandex.ru/'
    browser_name: Literal['chrome', 'firefox'] = 'chrome'
    browser_version: str = '100.0'
    hold_driver_at_exit: bool = False
    headless: bool = False
    timeout: float = 5.0
    environment: Literal['local', 'remote'] = 'local'
    driver_remote_url: str = ''


settings = Settings()


