import allure
import config
from selene import have, browser

class LoginForm:
    @allure.step('Нажимаем на кнопку войти')
    def log_in(self):
        browser.element_by(have.text('Войти')).click()

    @allure.step('Вводим данные пользователя')
    def fill_user(self):
        pass


    #@allure.step('Нажимаем кнопку ')