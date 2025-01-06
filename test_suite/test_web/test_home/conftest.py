import pytest
import string
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from test_suite.driver_functions import *
import time
import allure

@allure.step("Going through the pop-ups at first launch")
@pytest.fixture
def web_driver_design(web_driver_home,test_logger):
    test_logger.info("Setting up web_driver_home")
    with allure.step("Going to the design page"):
        element_click(web_driver_home, By.CSS_SELECTOR, ".grid:nth-child(1) > .grid > .h-full > .w-10", test_logger=test_logger)

    yield web_driver_home
    # Any additional teardown logic can be added here

