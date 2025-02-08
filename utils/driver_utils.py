from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

class DriverUtils:
    @classmethod
    def get_driver(cls, headless=True):
        # 初始化 WebDriver
        service = Service('./drivers/geckodriver')
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Firefox(service=service, options=options)
        print("browserVersion:", driver.capabilities['browserVersion'])
        return driver

    @classmethod
    def close_driver(cls, driver):
        driver.quit()
