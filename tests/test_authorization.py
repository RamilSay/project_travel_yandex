import allure
import pytest
from allure_commons.types import Severity
from selene import browser

import config
from ui_model.pages.login_form import LoginForm
from ui_model.pages.main_page import MainPage

main_page = MainPage()
login_form = LoginForm()


@allure.label('owner', 'ramilsay')
@allure.tag('UI')
@allure.tag('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.title('Проверяем авторизацию пользователя')
def test_login():
    main_page.open_main_page()
    login_form.log_in()
    login_form.fill_user()
    login_form.should_wrong_message()






@allure.severity(Severity.BLOCKER)
@allure.title('Авторизация пользователя с некорректными данными')
@pytest.mark.web
@pytest.mark.user
def test_incorrect_login(open_browser):
    login_page = Login(
        user=UserModel(email='incorrect@mail.ru', password='incorrect_password')
    )
    login_page.open()
    login_page.fill_form()
    login_page.submit()
    login_page.check_result_after_incorrect_login_data('Incorrect username or password')