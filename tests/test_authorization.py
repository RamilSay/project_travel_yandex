import time

import allure
import pytest
from allure_commons.types import Severity
from selene import have, browser

import config
from data.user import User
from ui_model.pages.login_form import LoginForm
from ui_model.pages.main_page import MainPage

main_page = MainPage()


@allure.label('owner', 'ramilsay')
@allure.tag('UI')
@allure.feature('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.epic('UI tests')
@allure.title('Authorization is impossible with incorrect login and password')
@pytest.mark.ui
@pytest.mark.user
def test_incorrect_login(browser_management):
    page = LoginForm(user=User('', ''))
    main_page.open_main_page()
    page.click_button_log_in()
    page.fill_user()
    page.should_error_message('Неверный пароль')


@allure.label('owner', 'ramilsay')
@allure.tag('UI')
@allure.feature('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.epic('UI tests')
@allure.title('Authorization with correct login and password')
def test_login(user_for_auth):
    page = LoginForm(user_for_auth)
    main_page.open_main_page()
    page.click_button_log_in()
    page.fill_user()
    # assert login_form.should_error_message() == 'Неверный пароль'

# login_page = Login(
# user=UserModel(email='incorrect@mail.ru', password='incorrect_password')
# )
