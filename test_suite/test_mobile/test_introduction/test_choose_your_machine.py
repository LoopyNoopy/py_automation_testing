from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from test_suite.driver_functions import *
from appium.webdriver.common.appiumby import AppiumBy
import allure
import time


@allure_suite("mobile_app_name", "Introduction", "Choose your machine", "Test for selecting the machine_name 2 in the introduction")
@allure_story("mobile_app_name","Machine Setup","Choose machine in Introduction")
@allure_attributes(
    "Test for choosing your machine",
    ["Introduction","Machine Selection","machine_name 2"],
    allure.severity_level.CRITICAL,
    "Daniel Burgess"
)
def test_curio2(mobile_driver, test_logger):
    element_click(mobile_driver,AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Accept\")", test_logger)
    element_click(mobile_driver, AppiumBy.ACCESSIBILITY_ID, "SkipButton", test_logger)
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"machine_name 2\")", test_logger)
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.Button\").instance(1)", test_logger)
    element = element_wait(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR,
                           "new UiSelector().text(\"Tray Type: Electrostatic Tray\")", test_logger)
    assert element and element.text == "Tray Type: Electrostatic Tray"


@allure_suite("mobile_app_name", "Introduction", "Choose your machine", "Test for selecting the machine_name 5 Plus in the introduction")
@allure_story("mobile_app_name","Machine Setup","Choose machine in Introduction")
@allure_attributes(
    "Test for choosing your machine",
    ["Introduction","Machine Selection","machine_name 5 Plus"],
    allure.severity_level.CRITICAL,
    "Daniel Burgess"
)
def test_cameo5_plus(mobile_driver, test_logger):
    element_click(mobile_driver,AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Accept\")", test_logger)
    element_click(mobile_driver, AppiumBy.ACCESSIBILITY_ID, "SkipButton", test_logger)
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"machine_name 5 Plus\")", test_logger)
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.Button\").instance(1)", test_logger)
    element = element_wait(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR,
                           "new UiSelector().text(\"Mat Size: machine_name Plus (15 x 15 in)\")", test_logger)
    assert element and element.text == "Mat Size: machine_name Plus (15 x 15 in)"


@allure_suite("mobile_app_name", "Introduction", "Choose your machine", "Test for selecting the machine_name 5 in the introduction")
@allure_story("mobile_app_name","Machine Setup","Choose machine in Introduction")
@allure_attributes(
    "Test for choosing your machine",
    ["Introduction","Machine Selection","machine_name 5"],
    allure.severity_level.CRITICAL,
    "Daniel Burgess"
)
def test_cameo5(mobile_driver, test_logger):
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Accept\")", test_logger)
    element_click(mobile_driver, AppiumBy.ACCESSIBILITY_ID, "SkipButton", test_logger)
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"machine_name 5\")", test_logger)
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR,
                  "new UiSelector().className(\"android.widget.Button\").instance(1)", test_logger)
    element = element_wait(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR,
                           "new UiSelector().text(\"Mat Size: machine_name (12 x 12 in)\")", test_logger)
    assert element and element.text == "Mat Size: machine_name (15 x 15 in)"


@allure_suite("mobile_app_name", "Introduction", "Choose your machine", "Test for selecting the machine_name Pro Mkii in the introduction")
@allure_story("mobile_app_name","Machine Setup","Choose machine in Introduction")
@allure_attributes(
    "Test for choosing your machine",
    ["Introduction","Machine Selection","machine_name Pro Mkii"],
    allure.severity_level.CRITICAL,
    "Daniel Burgess"
)
def test_cameo_pro_mkii(mobile_driver, test_logger):
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Accept\")", test_logger)
    element_click(mobile_driver, AppiumBy.ACCESSIBILITY_ID, "SkipButton", test_logger)
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"CAMEO Pro MK-II\")", test_logger)
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR,
                  "new UiSelector().className(\"android.widget.Button\").instance(1)", test_logger)
    element = element_wait(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR,
                           "new UiSelector().text(\"Mat Size: machine_name Pro (24 x 24 in)\")", test_logger)
    assert element and element.text == "Mat Size: machine_name Pro (24 x 14 in)"


@allure_suite("mobile_app_name", "Introduction", "Choose your machine", "Test for selecting the machine_name 4 in the introduction")
@allure_story("mobile_app_name","Machine Setup","Choose machine in Introduction")
@allure_attributes(
    "Test for choosing your machine",
    ["Introduction","Machine Selection","machine_name 4"],
    allure.severity_level.CRITICAL,
    "Daniel Burgess"
)
def test_portrait4(mobile_driver, test_logger):
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Accept\")", test_logger)
    element_click(mobile_driver, AppiumBy.ACCESSIBILITY_ID, "SkipButton", test_logger)
    element_wait(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR,
                 "new UiSelector().text(\"Choose Your Machine\")", test_logger)
    actions = ActionChains(mobile_driver)
    actions.w3c_actions = ActionBuilder(mobile_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(1221, 1051)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(1225, 237)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"machine_name 4\")", test_logger)
    element_click(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR,
                  "new UiSelector().className(\"android.widget.Button\").instance(1)", test_logger)
    element = element_wait(mobile_driver, AppiumBy.ANDROID_UIAUTOMATOR,
                           "new UiSelector().text(\"Mat Size: machine_name 4 (8.5 x 12 in)\")", test_logger)
    assert element and element.text == "Mat Size: machine_name 4 (8.5 x 12 in)"
