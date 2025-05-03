import allure  # Импортируем библиотеку Allure для добавления шагов и логирования результатов в отчеты тестирования
from base.base_page import BasePage  # Импортируем базовый класс BasePage для наследования функциональности страниц
from config.links import Links  # Импортируем класс Links, который содержит URL-адреса страниц приложения
from selenium.webdriver.support import expected_conditions as EC  # Импортируем условия ожидания из Selenium для определения состояния элементов

class DashboardPage(BasePage):  # Определяем класс DashboardPage, который наследует функциональность базового класса BasePage

    PAGE_URL = Links.DASHBOARD_PAGE  # Задаем URL главной страницы (Dashboard) из класса Links

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")  # Определяем локатор для кнопки "My Info" с использованием XPath

    @allure.step("Click on 'My Info' link")  # Добавляем шаг в отчет Allure с описанием действия
    def click_my_info_link(self):  # Метод для клика на ссылку "My Info"
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()  # Ждем, пока кнопка "My Info" станет кликабельной, и выполняем клик