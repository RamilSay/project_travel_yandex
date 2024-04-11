import allure
from selene import be, have, browser


class MainPage:
    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        browser.open('/')

    @allure.step('Нажимаем на кнопку войти')
    def authorization(self):
        browser.element_by(have.text('Войти'))
