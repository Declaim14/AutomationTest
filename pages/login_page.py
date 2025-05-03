import allure  # Импортируем библиотеку Allure для добавления шагов и логирования результатов в отчеты тестирования
from base.base_page import BasePage  # Импортируем базовый класс BasePage для наследования функциональности страниц
from config.links import Links  # Импортируем класс Links, который содержит URL-адреса страниц приложения
from selenium.webdriver.support import expected_conditions as EC  # Импортируем условия ожидания из Selenium для определения состояния элементов

class LoginPage(BasePage):  # Определяем класс LoginPage, который наследуется от базового класса BasePage

    PAGE_URL = Links.LOGIN_PAGE  # Задаем URL страницы входа из класса Links

    USERNAME_FIELD = ("xpath", "//input[@name='username']")  # Определяем локатор для поля ввода имени пользователя с использованием XPath
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")  # Определяем локатор для поля ввода пароля с использованием XPath
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")  # Определяем локатор для кнопки отправки формы с использованием XPath

    @allure.step("Enter login")  # Добавляем шаг в отчет Allure с описанием, что выполняется ввод имени пользователя
    def enter_login(self, login):  # Метод для ввода логина
        # Ожидаем, пока поле имени пользователя станет кликабельным, и вводим логин
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")  # Добавляем шаг в отчет Allure с описанием, что выполняется ввод пароля
    def enter_password(self, password):  # Метод для ввода пароля
        # Ожидаем, пока поле пароля станет кликабельным, и вводим пароль
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")  # Добавляем шаг в отчет Allure с описанием, что выполняется клик по кнопке отправки
    def click_submit_button(self):  # Метод для клика по кнопке отправки
        # Ожидаем, пока кнопка отправки станет кликабельной, и выполняем клик
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()