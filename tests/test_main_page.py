import time
import pytest

import allure
from allure_commons.types import Severity

from ui_model.pages.main_page import MainPage

main_page = MainPage()


@allure.label('owner', 'ramilsay')
@allure.severity(Severity.CRITICAL)
@allure.epic('UI tests')
@allure.tag('Main menu')
@allure.title('Проверяем главную страницу')
@pytest.mark.parametrize('browser_management', ['firefox'], indirect=True)
def test_main_page(browser_management):
    main_page.open()
    time.sleep(12)
    main_page.clickable_log_in()
    main_page.should_label_main_menu_be_clickable()
    main_page.should_main_menu_correct()
    main_page.should_find_field_works('Москва', 22, 28)
    time.sleep(7)


