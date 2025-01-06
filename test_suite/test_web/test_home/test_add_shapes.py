from test_suite.driver_functions import *
import allure


@allure_suite("website_name", "Design", "Add Shapes", "Add Square")
@allure_story("website_name","Shapes","Adding Shapes")
@allure_attributes(
    "Test for adding a square",
    ["Add Shapes","Square"],
    allure.severity_level.BLOCKER,
    "Daniel Burgess"
)
def test_add_square(web_driver_design, test_logger):
    test_logger.warning("IM A WARNING")
    element_click(web_driver_design, By.CSS_SELECTOR, ".justify-end > .text-white", test_logger)
    element_click(web_driver_design, By.ID, "imageId", test_logger)
    with allure.step("Clicking on the square"):
        element_click(web_driver_design, By.CSS_SELECTOR, ".grid > .bg-white:nth-child(1) > img", test_logger)
    # ToDo - Add assert for either square in file or by screenshot comparison using either SauceLabs or AppliTools Eyes

@allure_suite("website_name", "Design", "Add Shapes", "Add Circle")
@allure_story("website_name","Shapes","Adding Shapes")
@allure_attributes(
    "Test for adding a circle",
    ["Add Shapes","Circle"],
    allure.severity_level.BLOCKER,
    "Daniel Burgess"
)
def test_add_circle(web_driver_design, test_logger):
    element_click(web_driver_design, By.CSS_SELECTOR, ".justify-end > .text-white", test_logger)
    element_click(web_driver_design, By.ID, "imageId", test_logger)
    with allure.step("Clicking on the circle"):
        element_click(web_driver_design, By.CSS_SELECTOR, ".grid:nth-child(1) > .grid > .grid:nth-child(2) > .object-contain", test_logger)
    # ToDo - Add assert for either square in file or by screenshot comparison using either SauceLabs or AppliTools Eyes


@allure_suite("website_name", "Design", "Add Shapes", "Add Star")
@allure_story("website_name","Shapes","Adding Shapes")
@allure_attributes(
    "Test for adding a star",
    ["Add Shapes","Star"],
    allure.severity_level.BLOCKER,
    "Daniel Burgess"
)
def test_add_star(web_driver_design, test_logger):
    element_click(web_driver_design, By.CSS_SELECTOR, ".justify-end > .text-white", test_logger)
    element_click(web_driver_design, By.ID, "imageId", test_logger)
    with allure.step("Clicking on star"):
        element_click(web_driver_design, By.CSS_SELECTOR, ".grid:nth-child(1) > .grid > .grid:nth-child(3) > .object-contain", test_logger)
    # ToDo - Add assert for either square in file or by screenshot comparison using either SauceLabs or AppliTools Eyes


@allure_suite("website_name", "Design", "Add Shapes", "Add Heart")
@allure_story("website_name","Shapes","Adding Shapes")
@allure_attributes(
    "Test for adding a Heart",
    ["Add Shapes","Heart"],
    allure.severity_level.BLOCKER,
    "Daniel Burgess"
)
def test_add_heart(web_driver_design, test_logger):
    element_click(web_driver_design, By.CSS_SELECTOR, ".justify-end > .text-white", test_logger)
    element_click(web_driver_design, By.ID, "imageId", test_logger)
    with allure.step("Clicking on the heart"):
        element_click(web_driver_design, By.CSS_SELECTOR, ".grid:nth-child(1) > .grid > .grid:nth-child(4) > .object-contain", test_logger)
    # ToDo - Add assert for either square in file or by screenshot comparison using either SauceLabs or AppliTools Eyes


@allure_suite("website_name", "Design", "Add Shapes", "Add Semi-circle")
@allure_story("website_name","Shapes","Adding Shapes")
@allure_attributes(
    "Test for adding a semi-circle",
    ["Add Shapes","Semi-circle"],
    allure.severity_level.BLOCKER,
    "Daniel Burgess"
)
def test_add_semicircle(web_driver_design, test_logger):
    element_click(web_driver_design, By.CSS_SELECTOR, ".justify-end > .text-white", test_logger)
    element_click(web_driver_design, By.ID, "imageId", test_logger)
    with allure.step("Clicking on the semi-circle"):
        element_click(web_driver_design, By.CSS_SELECTOR, ".grid:nth-child(5)", test_logger)
    # ToDo - Add assert for either square in file or by screenshot comparison using either SauceLabs or AppliTools Eyes
