from pages.base_page import BasePage
from utils.driver_utils import DriverUtils
from selenium.webdriver.common.by import By
from crontab import CronTab
import os
import pyotp

def login():
    # 0. prepare
    driver = DriverUtils.get_driver()
    base_url = os.getenv('BASE_URL') or ""
    username = os.getenv('USERNAME') or ""
    password = os.getenv('PASSWORD') or ""
    totp_secret = os.getenv('TOTP_SECRET') or ""

    # 1. open login page
    page = BasePage(driver)
    page.open(base_url + "/login")
    driver.implicitly_wait(10)

    # 2. input username and password
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys(username)
    password_input.send_keys(password)

    # 3. click login button
    span_element = driver.find_element(By.XPATH, "//span[text()='登 錄']")
    login_button= span_element.find_element(By.XPATH, "./ancestor::button")
    login_button.click()

    # 4. input otp code
    otp_code_input= driver.find_element(By.ID, "otpCode")
    totp = pyotp.TOTP(totp_secret)
    totp_code = totp.now()
    otp_code_input.send_keys(totp_code)

    # 5. click verify button
    span_element = driver.find_element(By.XPATH, "//span[text()='???']")
    login_button= span_element.find_element(By.XPATH, "./ancestor::button")
    login_button.click()

    # 6. close driver
    DriverUtils.close_driver(driver)

if __name__ == "__main__":
    cron = CronTab(user='root')
