import random  # Импортируем модуль random для генерации случайных чисел
import allure  # Импортируем библиотеку Allure для добавления шагов и логирования результатов в отчеты тестирования
import pytest  # Импортируем библиотеку pytest для написания тестов
from base.base_test import BaseTest   # Импортируем базовый класс BaseTest, содержащий общую функциональность для тестов

@allure.feature("Profile Functionality")  # Указываем, что тест относится к функциональности профиля
class TestProfileFeature(BaseTest):  # Определяем класс для тестирования функциональности профиля, наследуя от BaseTest



    @allure.title("Change profile name")  # Указываем название теста, которое будет отображаться в отчете Allure
    @allure.severity("Critical")  # Устанавливаем уровень серьезности теста как критический
    @pytest.mark.smoke  # Помечаем тест как дымовой тест, который можно использовать для быстрого прогонов тестов
    def test_change_profile_name(self):  # Метод для теста изменения имени профиля
        self.login_page.open()   # Открываем страницу входа
        self.login_page.enter_login(self.data.LOGIN)  # Вводим логин из данных
        self.login_page.enter_password(self.data.PASSWORD)  # Вводим пароль из данных
        self.login_page.click_submit_button()  # Кликаем по кнопке отправки формы входа
        self.dashboard_page.is_opened()  # Проверяем, что главная панель управления открыта
        self.dashboard_page.click_my_info_link()  # Кликаем по ссылке "My Info"
        self.personal_page.is_opened()  # Проверяем, что страница личного профиля открыта
        self.personal_page.change_name(f"Test {random.randint(1, 5)}")  # Меняем имя профиля на случайное значение
        self.personal_page.save_changes()  # Сохраняем изменения
        self.personal_page.is_changes_saved()  # Проверяем, были ли изменения успешно сохранены


