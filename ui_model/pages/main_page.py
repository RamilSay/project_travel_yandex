import allure
from selene import be, by, have, browser


class MainPage:
    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        browser.open('https://travel.yandex.ru/')

    @allure.step('Проверяем кликабельность кнопки Войти')
    def clickable_log_in(self):
        browser.element('.WvMZr').should(be.clickable)

    @allure.step('Проверяем лейбл Путешествия')
    def should_label_be_clickable_and_have_text(self):
        browser.element('/a').should(be.visible).should(have.text('Перейти на главную Яндекс Путешествий')).click()

    @allure.step('Проверяем верхнее меню')
    def should_main_menu_titles(self):
        browser.all('.tm-main-menu__item').should(
            have.exact_texts('Моя лента',
                             'Все потоки',
                             'Разработка',
                             'Администрирование',
                             'Дизайн',
                             'Менеджмент',
                             'Маркетинг',
                             'Научпоп'
                             )
        )

    @allure.step('Проверяем подвал сайта')
    def should_footer_menu_titles(self):
        browser.all('.tm-footer-menu__block-title').should(
            have.exact_texts('Ваш аккаунт',
                             'Разделы',
                             'Информация',
                             'Услуги')
        )
