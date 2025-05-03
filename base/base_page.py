import allure  # Импорт библиотеки Allure для добавления шагов и логирования результатов в отчеты
from allure_commons.types import AttachmentType  # Импорт типов вложений для Allure, в данном случае для изображений
from selenium.webdriver.support.ui import WebDriverWait  # Импорт класса для ожидания выполнения условий в WebDriver
from selenium.webdriver.support import expected_conditions as EC  # Импорт пространства имен для заданных ожиданий

class BasePage:  # Определение базового класса для страниц приложения

    def __init__(self, driver):  # Конструктор класса, который принимает объект драйвера
        self.driver = driver  # Сохраняем драйвер в качестве атрибута экземпляра для последующего использования
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)  # Создаем экземпляр WebDriverWait с тайм-аутом 10 секунд и частотой проверки 1 секунду


    def open(self):  # Метод для открытия страницы
        with allure.step(f"Open {self.PAGE_URL} page"):  # Используем Allure, чтобы задать шаг в отчете с URL страницы
            self.driver.get(self.PAGE_URL)  # Открываем страницу по указанному URL


    def is_opened(self):  # Метод для проверки, что страница открыта
        with allure.step(f"Open {self.PAGE_URL} is opened"):  # Создаем шаг в отчете, описывающий действие
            self.wait.until(EC.url_to_be(self.PAGE_URL))  # Ждем, пока текущий URL не совпадет с URL страницы


    def make_screenshot(self, screenshot_name):  # Метод для создания снимка экрана
        allure.attach(  # Используем Allure для прикрепления изображения в отчет
            body=self.driver.get_screenshot_as_png(),  # Получаем снимок экрана в формате PNG
            name=screenshot_name,  # Имя для снимка, которое будет показано в отчете
            attachment_type=AttachmentType.PNG  # Указываем тип вложения как PNG
        )
