import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session",autouse=True)
def set_driver():
    options = AppiumOptions()
    caps = {}
    caps["platformName"] = "Android"
    caps["appium:platformVersion"] = "11"
    caps["appium:automationName"] = "UIAutomator2"
    caps["appium:noReset"] = True
    caps["appium:ensureWebviewsHavePages"] = True
    caps["appium:nativeWebScreenshot"] = True
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:connectHardwareKeyboard"] = True

    options.load_capabilities(caps)

    driver = webdriver.Remote("http://127.0.0.1:4325", options=options)
    yield driver
    driver.quit()