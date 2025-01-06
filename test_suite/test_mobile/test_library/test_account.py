from appium.webdriver.common.appiumby import AppiumBy
from test_suite.driver_functions import *
import allure


@allure_suite("Mobile app", "Library", "Account")
@allure_story("Mobile app","Library","Signing in")
@allure_attributes(
    "Test for signing in",
    ["Library","Account","Sign in"],
    allure.severity_level.CRITICAL,
    "Daniel Burgess"
)
def test_sign_in(library_mobile_driver, test_logger):
    assert True
