import allure
from allure_commons.types import Severity

from ui_model.pages.main_page import MainPage

main_page = MainPage()


@allure.label('owner', 'ramilsay')
@allure.tag('UI')
@allure.tag('Main menu')
@allure.severity(Severity.CRITICAL)
@allure.title('Проверяем главную страницу')
def test_main_page():
    main_page.open()
    main_page.clickable_log_in()
    main_page.should_label_main_menu_be_clickable()
    main_page.should_main_menu_correct()
        # main_page.should_main_menu_titles()
    # main_page.should_footer_menu_titles()
