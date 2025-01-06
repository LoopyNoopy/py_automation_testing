import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from test_suite.driver_functions import *
from applitools.selenium import Target

@allure_suite("website_name", "Design", "Move Shapes", "Move Star")
@allure_story("website_name","Shapes","Moving Shapes")
@allure_attributes(
    "Test for click and dragging a square",
    ["Move Shapes","square","Click and Drag"],
    allure.severity_level.CRITICAL,
    "Daniel Burgess"
)
def test_move_star(web_driver_design, eyes, test_logger):
    original_size = (868, 1020)

    # Open Applitools Eyes for visual testing
    eyes.open(web_driver_design, "Example App", "Move Star Test", {"width": 1024, "height": 768})

    # Perform the series of actions
    element_click(web_driver_design, By.CSS_SELECTOR, ".grid:nth-child(1) > .grid > .hidden > .uppercase", test_logger)
    element_click(web_driver_design, By.CSS_SELECTOR, ".justify-end > .text-white", test_logger)
    element_click(web_driver_design, By.ID, "imageId", test_logger)
    element_click(web_driver_design, By.CSS_SELECTOR, ".grid:nth-child(1) > .grid > .grid:nth-child(3) > .grid", test_logger)
    element_click(web_driver_design, By.CSS_SELECTOR, ".guide-hoverable:nth-child(1) > #imageId .no__highlights", test_logger)

    element_click_and_drag(web_driver_design,
                           [(By.ID, "designCanvas", (201.84375, 226)),
                            (By.ID, "designCanvas", (536.84375, 614))], test_logger,
                           original_size)

    element_click(web_driver_design, By.ID, "designCanvas", test_logger)

    # Visual checkpoint before performing the drag-and-drop
    eyes.check("Before Drag and Drop", Target.window())

    # Perform the drag-and-drop action
    element_click_and_drag(web_driver_design,
                           [(By.ID, "designCanvas", (201.84375, 226)),
                            (By.ID, "designCanvas", (536.84375, 614))], test_logger,
                           original_size)

    # Visual checkpoint after performing the drag-and-drop
    eyes.check("After Drag and Drop", Target.window())

    # Close Applitools Eyes
    eyes.close_async()
