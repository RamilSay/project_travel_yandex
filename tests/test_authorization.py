import time

import allure
import pytest
from allure_commons.types import Severity
from data.user import User
from ui_model.pages.login_form import LoginForm
from ui_model.pages.main_page import MainPage

main_page = MainPage()


@allure.label('owner', 'ramilsay')
@allure.severity(Severity.BLOCKER)
@allure.epic('UI тесты')
@allure.feature('Авторизация')
@allure.title('Авторизация невозможна с некорректными логином и паролем')
@pytest.mark.ui
@pytest.mark.test_user
@pytest.mark.parametrize('browser_management', ['chrome'], indirect=True)
def test_incorrect_login(browser_management):
    page = LoginForm(user=User('', 'test'))
    main_page.open()
    page.click_button_log_in()
    page.fill_user()
    page.should_error_message('Неверный пароль')


@allure.label('owner', 'ramilsay')
@allure.severity(Severity.BLOCKER)
@allure.epic('UI тесты')
@allure.feature('Авторизация')
@allure.title('Авторизация с корректными логином и паролем')
@pytest.mark.ui
@pytest.mark.user
@pytest.mark.parametrize('browser_management', ['chrome'], indirect=True)
def test_login(browser_management, user_for_auth):
    page = LoginForm(user_for_auth)
    main_page.open()
    page.click_button_log_in()
    page.fill_user()
    #time.sleep(15)  # тайм-аут для ввода капчи
    page.should_menu_user_show()
    page.should_main_menu_show()
    page.click_button_log_out()
    page.should_main_menu_show()
    time.sleep(10)
