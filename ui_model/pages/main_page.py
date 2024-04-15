import allure
from selene import be, by, have, browser
import requests

from config import Config


class MainPage:
    def __init__(self):
        self.button_log_in = browser.element('.WvMZr')
        self.url = Config().base_url

    @allure.step('Открываем главную страницу')
    def open(self):
        browser.open(self.url)

    @allure.step('Проверяем кликабельность кнопки Войти')
    def clickable_log_in(self):
        self.button_log_in.should(be.clickable)

    @allure.step('Проверяем лэйбл главного меню')
    def should_label_main_menu_be_clickable(self):
        browser.element('.hE6MR').should(be.visible).click()

    @allure.step('Проверяем, что главная страница отображается корректно')
    def should_main_menu_correct(self):
        response = requests.request('get', self.url)
        assert response.status_code == 300

    @allure.step('Проверяем подвал сайта')
    def should_footer_menu_titles(self):
        browser.all('.tm-footer-menu__block-title').should(
            have.exact_texts('Ваш аккаунт',
                             'Разделы',
                             'Информация',
                             'Услуги')
        )
