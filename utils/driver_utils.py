from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

class DriverUtils:
    @classmethod
    def get_driver(cls):
        # 初始化 WebDriver
        service = Service('./drivers/geckodriver')
        options = Options()
        driver = webdriver.Firefox(service=service, options=options)
        return driver

    @classmethod
    def close_driver(cls, driver):
        # 关闭 WebDriver
        driver.quit()
