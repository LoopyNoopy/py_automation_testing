from appium.webdriver.common.appiumby import AppiumBy
import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

pytestmark = pytest.mark.demo


def element_wait(mobile_driver, by_type, finder_value, timeout=120):
    wait = WebDriverWait(mobile_driver, timeout=timeout)
    try:
        element = wait.until(EC.presence_of_element_located((by_type, finder_value)))
        print("Element found:", element.text)
    except Exception as e:
        print("Element not found within the specified time")
    return


@allure.parent_suite("Library Testing")
@allure.suite("Sign in test")
def test_signin(mobile_driver):
    assert mobile_driver is not None, "mobile_driver should not be None"
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.Button[@text=\"Accept\"]")
    el1 = mobile_driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Accept\"]")
    el1.click()
    time.sleep(5)
    el2 = mobile_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SkipButton")
    el2.click()
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.TextView[@text=\"Curio 2\"]")
    el3 = mobile_driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Curio 2\"]")
    el3.click()
    element_wait(mobile_driver, AppiumBy.XPATH,
                 "//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton")
    el4 = mobile_driver.find_element(by=AppiumBy.XPATH,
                                     value="//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton")
    el4.click()
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.TextView[@text=\"Sign in\"]")
    el5 = mobile_driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Sign in\"]")
    el5.click()
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.EditText[@text=\"Email\"]")
    el6 = mobile_driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Email\"]")
    el6.send_keys("")
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.EditText[@text=\"Password\"]")
    el7 = mobile_driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Password\"]")
    el7.send_keys("")
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.Button[@text=\"Sign In\"]")
    el8 = mobile_driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Sign In\"]")
    el8.click()
    element_wait(mobile_driver, AppiumBy.XPATH, "//*[contains(@text, 'Send')]")
    el9 = mobile_driver.find_element(by=AppiumBy.XPATH,
                                     value="//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton")
    el9.click()
    element_wait(mobile_driver, AppiumBy.XPATH, "//android.widget.TextView[@text=\"d20@aspexsoftware.com\"]")
    el20 = mobile_driver.find_element(by=AppiumBy.XPATH,
                                      value="//android.widget.TextView[@text=\"d20@aspexsoftware.com\"]")
    assert el20.text == "d20@aspexsoftware.com"


@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 3), (2, 3, 5), (5, 5, 10)])
def test_addition354(request, num1, num2, expected):
    result = num1 + num2
    assert result == expected
