import os
import pytest

from data.user import User
"""
from utils import attach
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
"""
from dotenv import load_dotenv

load_dotenv()

DEFAULT_BROWSER_VERSION = '100'
BASE_URL = 'https://travel.yandex.ru/'


def pytest_addoption(parser):
    parser.addoption('--browser_name', help='Браузер для тестов',
                     choices=['firefox', 'chrome'], default='chrome')
    parser.addoption('--browser_version', help='Версия браузера', default='100.0')

"""
@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser.config.base_url = BASE_URL
    browser_name = request.config.getoption('--browser_name')
    browser_version = request.config.getoption('--browser_version')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    options = webdriver.ChromeOptions()
    browser.config.driver_options = options

    options = Options()
    selenoid_capabilities = {
        'browserName': f'{browser_name}',
        'browserVersion': f'{browser_version}',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')

    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
"""


@pytest.fixture()
def user_for_auth():
    return User(email=os.getenv('EMAIL'), password=os.getenv('PASSWORD'))
