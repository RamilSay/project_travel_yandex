import os
import pytest
import config

from data.user import User

from utils import attach
from selene import browser
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions

from dotenv import load_dotenv

load_dotenv()

DEFAULT_BROWSER = 'chrome'
DEFAULT_BROWSER_VERSION = '100'
BASE_URL = 'https://travel.yandex.ru/'


@pytest.fixture()
def user_for_auth():
    return User(email=os.getenv('EMAIL'), password=os.getenv('PASSWORD'))


def pytest_addoption(parser):
    parser.addoption('--browser_name', help='Браузер для тестов',
                     choices=['firefox', 'chrome'], default='chrome')
    parser.addoption('--browser_version', help='Версия браузера', default='100.0')


"""
@pytest.fixture(scope="session", autouse=True)
def browser_setup():
    browser.config.timeout = 5.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()
"""


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser.config.base_url = BASE_URL
    if config.settings.environment == 'local':
        browser.config.window_width = 1920
        browser.config.window_height = 1080

        browser.config.driver_name = config.settings.browser_name \
            if config.settings.browser_name else DEFAULT_BROWSER
        browser.config.version = config.settings.browser_version \
            if config.settings.browser_version else DEFAULT_BROWSER_VERSION

    options = ChromeOptions() if browser.config.driver_name == 'chrome' \
        else FirefoxOptions()

    browser.config.driver_options = options

    browser_name = request.config.getoption('--browser_name')
    browser_version = request.config.getoption('--browser_version')

    if config.settings.environment == 'remote':
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





