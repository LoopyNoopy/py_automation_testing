# https://appium.io/docs/en/2.0/quickstart/
# https://www.youtube.com/watch?v=0WXRYqbUMZY
# adb shell dumpsys window | find "mCurrentFocus"

import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

caps = {}
caps["platformName"] = "iOS"
caps["appium:platformVersion"] = "16.5.1"
caps["appium:udid"] = "00008112-001548503487401E"
caps["appium:automationName"] = "XCUITest"
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = "3600"
caps["appium:connectHardwareKeyboard"] = True
caps["appium:xcodeOrgId"] = "TAX3B9PB9G"
caps["AddAdditionalCapability:app"] = "/Users/XXXX/abcd.app"
caps["appium:includeSafariInWebviews"] = True
appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        print("\nSetting up")
    def tearDown(self) -> None:
        print("\n Tearing down")

    def test_assert_fail_example(self) -> None:
        value = 1
        assert value == 3
    def test_assert_success_example(self) -> None:
        value = 1
        assert value == 1

if __name__ == '__main__':
    unittest.main()
