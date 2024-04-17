import allure
import config
from selene import be, by, have, browser

from data.user import User
from ui_model.pages.main_page import MainPage


class LoginForm:
    def __init__(self, user: User):
        self.user = user
        self.fill_login = browser.element('[name="login"]')
        self.fill_password = browser.element('[name="passwd"]')
        self.button_log_in = MainPage().button_log_in

    @allure.step('Нажимаем на кнопку Войти')
    def click_button_log_in(self):
        self.button_log_in.should(have.text('Войти')).click()

    @allure.step('Вводим данные пользователя')
    def fill_user(self):
        self.fill_login.type(self.user.email).press_enter()
        self.fill_password.type(self.user.password).press_enter()

    @allure.step('Проверяем сообщение об ошибке авторизации')
    def should_error_message(self, message_error: str):
        browser.element(by.text(message_error)).should(be.visible).should(have.text(message_error))

    @allure.step('Проверяем успешную авторизацию')
    def should_menu_user_show(self):
        browser.element('._3Tq3s rr1aS w9whJ').should(have.text('Открыть меню пользователя')).click()


    # @allure.step('Вводим невалидные данные пользователя')
    # fill_user()

    # @allure.step('Нажимаем кнопку')
