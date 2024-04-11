import requests
import pytest
import config
from utils import attach
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://habr.com'
    if config.ENVIRONMENT == 'local':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        options = webdriver.ChromeOptions()
        browser.config.driver_options = options
    else:
        options = Options()
        capabilities = {
            'browserName': 'chrome',
            'browserVersion': '100',
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }
        options.capabilities.update(capabilities)

        login = config.SELENOID_LOGIN
        password = config.SELENOID_PASSWORD

        driver = webdriver.Remote(
            command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
            options=options
        )
        browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    if config.ENVIRONMENT == 'remote':
        attach.add_video(browser)

    browser.quit()
