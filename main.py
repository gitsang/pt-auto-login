from pages.base_page import BasePage
from utils.driver_utils import DriverUtils
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import logging
import os
import pyotp

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def check_login(driver = None):
    if driver is None:
        driver = DriverUtils.get_driver()
    try:
        driver.find_element(By.XPATH, "//span[text()='當前活動']")
    except:
        return False
    return True

def login():
    # 0. prepare
    driver = DriverUtils.get_driver()
    driver.implicitly_wait(10)

    # 1. open login page
    logging.info("login...")
    page = BasePage(driver)
    page.open(base_url + "/login")

    # 2. input username and password
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys(username)
    password_input.send_keys(password)

    # 3. click login button
    span_element = driver.find_element(By.XPATH, "//span[text()='登 錄']")
    login_button= span_element.find_element(By.XPATH, "./ancestor::button")
    login_button.click()

    # 4. check if need otp code
    if check_login():
        logging.info("login success")
    else:
        # 4.1 input otp code
        logging.info("verifing otp...")
        otp_code_input= driver.find_element(By.ID, "otpCode")
        totp = pyotp.TOTP(totp_sec)
        totp_code = totp.now()
        otp_code_input.send_keys(totp_code)

        # 4.2 click verify button
        span_element = driver.find_element(By.XPATH, "//span[text()='???']")
        login_button= span_element.find_element(By.XPATH, "./ancestor::button")
        login_button.click()

        # 4.3 recheck if login success
        if check_login():
            logging.info("login success")
        else:
            logging.info("login failed")

    # 5. close driver
    logging.info("closing driver...")
    DriverUtils.close_driver(driver)

if __name__ == "__main__":
    # 0. load environment
    load_dotenv()
    base_url = os.getenv('BASE_URL') or ""
    username = os.getenv('USERNAME') or ""
    password = os.getenv('PASSWORD') or ""
    totp_sec = os.getenv('TOTP_SEC') or ""

    # 1. login
    login()
