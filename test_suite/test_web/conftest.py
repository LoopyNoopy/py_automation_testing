import pytest
import string
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from Testing.Smoke.test_core.driver_functions import element_wait
import time
import allure
from Testing.Smoke.test_core.driver_functions import element_send_keys, element_click

@allure.step("Going through the pop-ups at first launch")
@pytest.fixture
def web_driver_home(web_driver, browser_info, test_logger):
    browser_name = browser_info[0]  # Get the browser name

    with allure.step("Agreeing to beta dialogue"):
        element_click(web_driver, By.CSS_SELECTOR, ".rounded-btn-corners", test_logger=test_logger)

    with allure.step("Consenting to cookies"):
        element_click(web_driver, By.CSS_SELECTOR, ".grid:nth-child(1) > .red_hat_font_btn", test_logger=test_logger)

    # Closes the "Unsupported Browser" popup
    if browser_name != 'chrome':
        with allure.step("Closing 'Use Chrome' warning"):
            element_click(web_driver, By.XPATH, "//img[@alt='Close']", test_logger=test_logger)

    yield web_driver
    # Any additional teardown logic can be added here

