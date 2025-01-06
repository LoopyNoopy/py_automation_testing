import pytest
import string
from appium.webdriver.common.appiumby import AppiumBy
from Testing.Smoke.test_core.driver_functions import element_wait
import time
import allure

# Generate letters from 'a' to 'z'
letters = list(string.ascii_lowercase)

# Generate numbers from 1 to 99
numbers = list(range(1, 100))

# Combine letters and numbers into tuples
params = [(letter, number) for letter in letters for number in numbers]


def pytest_generate_tests(metafunc):
    if "letter" in metafunc.fixturenames and "number" in metafunc.fixturenames:
        metafunc.parametrize("letter, number", params)


@pytest.fixture
def library_mobile_driver(mobile_driver, test_logger):
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.Button[@text=\"Accept\"]", test_logger)
    el1 = mobile_driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Accept\"]")
    el1.click()
    time.sleep(5)
    el2 = mobile_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SkipButton")
    el2.click()
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.TextView[@text=\"Curio 2\"]", test_logger)
    el3 = mobile_driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Curio 2\"]")
    el3.click()
    element_wait(mobile_driver, AppiumBy.XPATH,
                 "//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton", test_logger)
    el4 = mobile_driver.find_element(by=AppiumBy.XPATH,
                                     value="//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton")
    el4.click()
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.TextView[@text=\"Sign in\"]", test_logger)
    el5 = mobile_driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Sign in\"]")
    el5.click()
    yield mobile_driver
    # Any additional teardown logic can be added here
