import allure
from allure_commons.types import Severity

from ui.pages.main_page import MainPage

main_page = MainPage()


@allure.label('owner', 'ramilsay')
@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем авторизацию пользователя')



@allure.step('Проверяем подвал сайта')
def should