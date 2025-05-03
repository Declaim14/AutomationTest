import allure  # Импортируем библиотеку Allure для добавления шагов и логирования результатов в отчеты тестирования
from selenium.webdriver.common.by import By  # Импортируем класс By для использования различных методов поиска элементов
from base.base_page import BasePage  # Импортируем базовый класс BasePage для наследования функциональности страниц
from config.links import Links  # Импортируем класс Links, который содержит URL-адреса страниц приложения
from selenium.webdriver.support import expected_conditions as EC  # Импортируем условия ожидания из Selenium для определения состояния элементов
from selenium.webdriver.common.keys import Keys  # Импортируем класс Keys для использования клавиш управления, таких как "Ctrl" и "Backspace"


class PersonalPage(BasePage):  # Определяем класс PersonalPage, который наследуется от базового класса BasePage

    PAGE_URL = Links.PERSONAL_PAGE  # Задаем URL страницы личного профиля из класса Links

    # Определяем локаторы для полей на странице с помощью XPath
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")  # Локатор для поля ввода имени
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")  # Локатор для кнопки сохранения изменений
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")  # Локатор для индикатора загрузки

    def change_name(self, new_name):  # Метод для изменения имени
        with allure.step(f"Change name on '{new_name}'"):  # Шаг в отчете Allure с описанием изменения имени
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))  # Ожидаем, пока поле ввода имени станет кликабельным

            # first_name_field.clear()  # Очистка поля ввода имени перед вводом нового значения
            first_name_field.send_keys(Keys.CONTROL + "a")  # Выделяем весь текст в поле
            first_name_field.send_keys(Keys.BACKSPACE)  # Удаляем выделенный текст
            assert first_name_field.get_attribute("value") == "", "There is text"  # Проверяем, что поле пустое
            first_name_field.send_keys(new_name)  # Вводим новое имя в поле
            self.name = new_name  # Сохраняем новое имя в атрибут класса для дальнейшего использования

    @allure.step("Save changes")  # Добавляем шаг в отчет Allure для сохранения изменений
    def save_changes(self):  # Метод для сохранения изменений
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()  # Ждем, пока кнопка сохранения станет кликабельной, и кликаем по ней

    @allure.step("Changes have been saved successfully")  # Шаг в отчете Allure для проверки успешного сохранения изменений
    def is_changes_saved(self):  # Метод для проверки, были ли изменения сохранены
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))  # Ждем, пока исчезнет индикатор загрузки
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))  # Ждем, пока поле имени станет видимым
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))  # Проверяем, что в поле отображается новое имя
