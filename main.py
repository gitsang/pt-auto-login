from pages.base_page import BasePage
from utils.driver_utils import DriverUtils
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import logging
import argparse
import os
import pyotp

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)


def check_login(driver=None):
    if driver is None:
        driver = DriverUtils.get_driver()
    try:
        driver.find_element(By.XPATH, "//span[text()='當前活動']")
    except:
        return False
    return True


def login(driver):
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
    login_button = span_element.find_element(By.XPATH, "./ancestor::button")
    login_button.click()

    # 4. check if need otp code
    if check_login(driver):
        logging.info("login success")
    else:
        # 4.1 input otp code
        logging.info("verifing otp...")
        otp_code_input = driver.find_element(By.ID, "otpCode")
        totp = pyotp.TOTP(totp_sec)
        totp_code = totp.now()
        otp_code_input.send_keys(totp_code)

        # 4.2 click verify button
        span_element = driver.find_element(By.XPATH, "//span[text()='登 錄']")
        login_button = span_element.find_element(By.XPATH, "./ancestor::button")
        login_button.click()

        # 4.3 recheck if login success
        if check_login(driver):
            logging.info("login success")
        else:
            logging.info("login failed")

    # 5. close driver
    logging.info("closing driver...")
    DriverUtils.close_driver(driver)


if __name__ == "__main__":
    # parse command line arguments
    parser = argparse.ArgumentParser(description="Login script")
    parser.add_argument("--base_url", type=str, help="Base URL for login")
    parser.add_argument("--username", type=str, help="Username for login")
    parser.add_argument("--password", type=str, help="Password for login")
    parser.add_argument("--totp_sec", type=str, help="TOTP secret for OTP")
    parser.add_argument(
        "--headless", type=bool, default=True, help="Enable headless mode"
    )
    args = parser.parse_args()

    # load environment variables
    load_dotenv()
    base_url = args.base_url or os.getenv("BASE_URL") or ""
    username = args.username or os.getenv("USERNAME") or ""
    password = args.password or os.getenv("PASSWORD") or ""
    totp_sec = args.totp_sec or os.getenv("TOTP_SEC") or ""
    headless = (
        args.headless
        if args.headless is not None
        else (os.getenv("HEADLESS", "True").lower() in ["true", "1", "t"])
    )

    # init driver
    driver = DriverUtils.get_driver(headless=headless)
    driver.implicitly_wait(10)

    # login
    login(driver)
