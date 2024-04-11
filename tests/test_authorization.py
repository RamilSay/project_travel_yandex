import allure
from allure_commons.types import Severity
from selene import browser

import config
from ui.pages.login_form import LoginForm
from ui.pages.main_page import MainPage

main_page = MainPage()
login_form = LoginForm()


@allure.label('owner', 'ramilsay')
@allure.tag('UI')
@allure.tag('Authorization')
@allure.severity(Severity.BLOCKER)
@allure.title('Проверяем авторизацию пользователя')
def test_login():
    main_page.open_main_page()