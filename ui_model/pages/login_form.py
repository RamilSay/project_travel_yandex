import allure
import config
from selene import be, by, have, browser

from data.user import User
from ui_model.pages.main_page import MainPage

main_page = MainPage()


class LoginForm:
    def __init__(self, user: User):
        self.user = user
        self.fill_login = browser.element('[name="login"]')
        self.fill_password = browser.element('[name="passwd"]')
        self.button_log_in = main_page.button_log_in
        self.button_log_out = main_page.button_log_out

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
        browser.element('(//span[@class="_1YbL5 Y0oJN N6eXh"])[1]').click()
        browser.element('(//span[@class="BUBpx PwvPC i9Gsh"])[1]').should(have.text(self.user.first_name))

    @allure.step('Проверяем, что находимся на главной странице')
    def should_main_menu_show(self):
        assert main_page.url == 'https://travel.yandex.ru/'

    @allure.step('Нажимаем на кнопку Выйти')
    def click_button_log_out(self):
        self.button_log_out.should(have.text('Выйти')).click()
        self.button_log_in.should(have.text('Войти'))
