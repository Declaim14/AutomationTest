import pytest  # Импортируем библиотеку pytest для организации тестирования
from selenium import webdriver  # Импортируем класс webdriver из Selenium для управления браузером
from selenium.webdriver.chrome.options import Options  # Импортируем класс Options для настройки параметров браузера Chrome

@pytest.fixture(scope="function", autouse=True)  # Определяем фикстуру pytest для настройки драйвера браузера, которая выполняется перед каждым тестом
def driver(request):  # Определяем функцию фикстуры, которая будет возвращать экземпляр драйвера
    options = Options()  # Создаем объект Options для настройки параметров Chrome
            # options.add_argument("--headless")  # Опционально: запускаем браузер в фоновом режиме (без графического интерфейса)
    options.add_argument("--no-sandbox")    # Опция, отключающая изоляцию (sandbox) для улучшения совместимости с CI/CD
    options.add_argument("--disable-dev-shm-usage")  # Опция, разрешающая использование общей памяти для контейнеров (например, Docker)
    options.add_argument("--window-size=1920x1080")  # Устанавливаем размер окна браузера
    driver = webdriver.Chrome(options=options)  # Создаем экземпляр драйвера Chrome с заданными параметрами
    request.cls.driver = driver  # Сохраняем экземпляр драйвера в классе теста, чтобы он был доступен в тестах
    yield driver  # Возвращаем экземпляр драйвера для использования в тестах
    driver.quit()  # Закрываем браузер после завершения тестов