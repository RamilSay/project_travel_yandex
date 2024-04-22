# Демонстрационный проект https://travel.yandex.ru/

<code><img width="5%" title="Python" src="design/icons/python.png"></code>
<code><img width="5%" title="Pytest" src="design/icons/pytest.png"></code>
<code><img width="5%" title="Selene" src="design/icons/selene.png"></code>
<code><img width="5%" title="Selenium" src="design/icons/selenium.png"></code>
<code><img width="5%" title="Selenoid" src="design/icons/selenoid.png"></code>
<code><img width="5%" title="Jenkins" src="design/icons/jenkins.png"></code>
<code><img width="5%" title="Jenkins" src="design/icons/allure_Report.svg"></code>

## Запуск тестов
### Запуск тестов локально
1. Клонировать репозиторий
```
git clone git@github.com:RamilSay/project_travel_yandex.git
```
2. Перейти в папку
```
cd pythonProject
```
3. Инициализировать виртуальное окружение
```
python -m venv venv
```
4. Активировать виртуальное окружение
```
source ./venv/bin/activate
```
5. Установить зависимости
```
pip install -r requirements.txt
```
6. Положить .env файл в папку с проектом
```
NAME = 'any_name'
EMAIL = 'any_email'
PASSWORD = 'any_password'

```
7. Запустить тесты
```
python -m pytest
```
## Allure отчеты

![image](https://github.com/RamilSay/project_travel_yandex.git/design/allure_ui_tests_#1_authorization.png)
![image](https://github.com/RamilSay/project_travel_yandex.git/design/allure_ui_tests_#2_authorization.png)
![image](https://github.com/RamilSay/project_travel_yandex.git/design/allure_ui_tests_#3_main_menu.png)
