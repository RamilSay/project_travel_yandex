import allure
import config
from selene import have, browser

from data.user import User


class LoginForm:
    def __init__(self, user: User):
        self.user = user
        self.fill_login = browser.element('[name="login"]')
        self.fill_password = browser.element('[name="passwd"]')
        self.message_error = browser.element('.Textinput-Hint Textinput-Hint_state_error')

    @allure.step('Click button Log_in')
    def click_button_log_in(self):
        browser.element('.WvMZr').should(have.text('Войти')).click()


    @allure.step('Вводим данные пользователя')
    def fill_user(self):
        self.fill_login.type(self.user.email).press_enter()
        self.fill_password.type(self.user.password).press_enter()

    @allure.step('Проверяем сообщение об ошибке ввода данных')
    def should_error_message(self, message_error: str):
        self.message_error.should(have.text(message_error))

        # raise ValueError('ERROR')

    # @allure.step('Вводим невалидные данные пользователя')
    # fill_user()

    # @allure.step('Нажимаем кнопку')
