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
SELENOID_LOGIN = 'user1'
SELENE_PASSWORD = 1234
```
7. Запустить тесты
```
python -m pytest
```
### Удаленный запуск проекта в Jenkins
Проект доступен по [ссылке](https://jenkins.autotests.cloud/job/C07-project_travel_yandex/), сборка и просмотр отчетов доступна для неавторизованных пользователей.
1. Открыть проект в Jenkins
2. Нажать "Собрать с параметрами"
<details><summary>screenshot</summary><img src=https://github.com/RamilSay/project_travel_yandex.git/design/icons/name></details>

## Отчеты

### Allure-отчет
Доступен по [ссылке](https://jenkins.autotests.cloud/job/C07-master_klinka-store_gaijin_demo/16/allure/)
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/82f540bf-cd90-49cc-b218-292c346a77a3)
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/6638c88b-71ee-40cd-a478-c92e8305eda3)
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/926d7d2e-c4ba-4304-a71a-03fa5d8c5878)
### Видео запуска теста
Браузеры запускаются удаленно на Selenide
![Watch the video](design/gif/test_video_example.gif)