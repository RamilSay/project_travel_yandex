import allure
import pytest
from allure_commons.types import Severity
from selene import have, browser

import config
from ui_model.pages.login_form import LoginForm
from ui_model.pages.main_page import MainPage

main_page = MainPage()
login_form = LoginForm()


@allure.label('owner', 'ramilsay')
@allure.tag('UI')
@allure.feature('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.epic('UI tests')
@allure.title('Authorization is impossible with incorrect login and password')
@pytest.mark.ui
@pytest.mark.user
def test_incorrect_login(open_browser):

    main_page.open_main_page()
    login_form.click_button_log_in()
    login_form.fill_user()
    login_form.should_error_message('Неверный пароль')


@allure.label('owner', 'ramilsay')
@allure.tag('UI')
@allure.feature('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.epic('UI tests')
@allure.title('Authorization with correct login and password')
def test_login():
    main_page.open_main_page()
    login_form.click_button_log_in()
    login_form.fill_user()
    #assert login_form.should_error_message() == 'Неверный пароль'

#login_page = Login(
        #user=UserModel(email='incorrect@mail.ru', password='incorrect_password')
    #)