import allure
import config
from selene import be, by, have, browser

from data.user import User


class LoginForm:
    def __init__(self, user: User):
        self.user = user
        self.fill_login = browser.element('[name="login"]')
        self.fill_password = browser.element('[name="passwd"]')

    @allure.step('Click button Log_in')
    def click_button_log_in(self):
        browser.element('.WvMZr').should(have.text('Войти')).click()

    @allure.step('Вводим данные пользователя')
    def fill_user(self):
        self.fill_login.type(self.user.email).press_enter()
        self.fill_password.type(self.user.password).press_enter()

    @allure.step('Проверяем сообщение об ошибке авторизации')
    def should_error_message(self, message_error: str):
        browser.element(by.text(message_error)).should(be.visible).should(have.text(message_error))
        #assert message_error == 'Неверный пароль'



    # @allure.step('Вводим невалидные данные пользователя')
    # fill_user()

    # @allure.step('Нажимаем кнопку')
