import pytest  # Импортируем библиотеку pytest для создания и выполнения тестов
from config.data import Data  # Импортируем класс Data из модуля config.data, который содержит тестовые данные
from pages.login_page import LoginPage  # Импортируем класс LoginPage для работы с элементами страницы входа
from pages.dashboard_page import DashboardPage  # Импортируем класс DashboardPage для работы с элементами главной панели управления
from pages.personal_page import PersonalPage  # Импортируем класс PersonalPage для работы с элементами страницы личного профиля

class BaseTest:  # Определяем базовый класс для тестов, от которого будут наследоваться другие тесты

    data: Data  # Объявляем атрибут data, который будет хранить тестовые данные
    login_page: LoginPage  # Объявляем атрибут login_page, который будет содержать экземпляр страницы входа
    dashboard_page: DashboardPage  # Объявляем атрибут dashboard_page, который будет содержать экземпляр главной панели управления
    personal_page: PersonalPage  # Объявляем атрибут personal_page, который будет содержать экземпляр страницы личного профиля

    @pytest.fixture(autouse=True)  # Используем фикстуру driver автоматически для всех тестов в этом классе
    def setup(self, request, driver):  # Метод для настройки, который выполняется перед каждым тестом
        request.cls.driver = driver  # Присваиваем экземпляр драйвера текущему классу, чтобы он был доступен во всех тестах
        request.cls.data = Data()  # Инициализируем тестовые данные и присваиваем атрибуту data
        request.cls.login_page = LoginPage(driver)  # Инициализируем страницу входа с помощью драйвера и присваиваем атрибуту login_page
        request.cls.dashboard_page = DashboardPage(driver)  # Инициализируем главную страницу с помощью драйвера и присваиваем атрибуту dashboard_page
        request.cls.personal_page = PersonalPage(driver)  # Инициализируем страницу личного профиля с помощью драйвера и присваиваем атрибуту personal_page