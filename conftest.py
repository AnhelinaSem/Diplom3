import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    web_driver = WebDriverFactory.get_driver(request.param)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark tests as smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: mark tests as regression tests"
    )
