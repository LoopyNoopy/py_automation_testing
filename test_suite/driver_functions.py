import socket
import pytest
import requests
from appium.options.common import AppiumOptions
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
import allure
import pytest
from functools import wraps


def allure_suite(parent_suite_name=None, suite_name=None, sub_suite_name=None, test_title=None):
    """
    Applies Allure suite metadata to a test function, including suite, parent suite, and sub suite.
    Allows dynamic titles with test parameters. Suite names are for file structure of the tests.

    :param parent_suite_name: str
        The name of the parent suite for hierarchical organization in the Allure report. Required.
    :param suite_name: str
        The name of the suite to which the test belongs. Required.
    :param sub_suite_name: str
        The name of the sub-suite for additional categorization within the Allure report. Required.
    :param test_title: str, optional
        The title of the test in the Allure report. Optional.

    :return: function
        The wrapped test function with applied Allure metadata.

    :raises: pytest.fail
        If any required parameter (parent_suite_name, suite_name, sub_suite_name) is missing.
    """

    def decorator(test_func):
        """
        Inner decorator function to wrap the test function, check for required parameters,
        and dynamically apply Allure labels if parameters are valid.

        :param test_func: function
            The test function to which the Allure suite metadata will be applied.

        :return: function
            The test function wrapped with Allure metadata, prepared for execution.
        """
        test_func._is_suited = True  # Mark the function as decorated

        @wraps(test_func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function that performs parameter validation, applies dynamic Allure labels,
            and sets the test title if provided.

            :param args: list
                Positional arguments passed to the test function.
            :param kwargs: dict
                Keyword arguments passed to the test function.

            :return: Any
                Returns the result of the test function execution if parameters are valid.

            :raises: pytest.fail
                Fails the test if any required parameter (except title) is None, preventing execution.
            """
            # Check if any required parameter is missing
            if suite_name is None or parent_suite_name is None or sub_suite_name is None:
                pytest.fail("All parameters (parent_suite_name, suite_name, sub_suite_name) must be provided.")

            # Apply Allure labels dynamically
            allure.dynamic.parent_suite(parent_suite_name)
            allure.dynamic.suite(suite_name)
            allure.dynamic.sub_suite(sub_suite_name)

            # Set the test title if provided
            if test_title:
                allure.dynamic.title(test_title)

            # Execute the test function
            return test_func(*args, **kwargs)

        return wrapper

    return decorator

def allure_story(epic_name=None, feature_name=None, story_name=None):
    """
    Applies Allure suite metadata to a test function, including suite, parent suite, sub-suite, and an optional title.
    Ensures all required parameters are provided. Allows dynamic titles with test parameters. Suite names are used for
    the hierarchical structure of the Allure report.

    :param epic_name: str
        The name of the epic (top-level grouping) in the Allure report. Required.
    :param feature_name: str
        The name of the feature (second-level grouping) to which the test belongs in the Allure report. Required.
    :param story_name: str
        The name of the story (third-level grouping) for additional categorization within the Allure report. Required.

    :return: function
        The wrapped test function with applied Allure metadata.

    :raises: pytest.fail
        If any required parameter (epic_name, feature_name, or story_name) is missing, causing the test to fail with a descriptive error.
    """


    def decorator(test_func):
        """
        Inner decorator function to wrap the test function, check for required parameters,
        and dynamically apply Allure labels if parameters are valid.

        :param test_func: function
            The test function to which the Allure suite metadata will be applied.

        :return: function
            The test function wrapped with Allure metadata, prepared for execution.
        """
        test_func._is_storied = True  # Mark the function as decorated

        @wraps(test_func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function that performs parameter validation, applies dynamic Allure labels,
            and sets the test title with parameter values if needed.

            :param args: list
                Positional arguments passed to the test function.
            :param kwargs: dict
                Keyword arguments passed to the test function.

            :return: Any
                Returns the result of the test function execution if parameters are valid.

            :raises: pytest.fail
                Fails the test if any required parameter (except title) is None, preventing execution.
            """
            # Check if any required parameter is missing (except title)
            if feature_name is None or epic_name is None or story_name is None:
                pytest.fail("All parameters (suite_name, parent_suite_name, sub_suite_name) must be provided.")

            # Apply Allure labels dynamically
            allure.dynamic.epic(epic_name)
            allure.dynamic.feature(feature_name)
            allure.dynamic.story(story_name)

            # Execute the test function
            return test_func(*args, **kwargs)

        return wrapper

    return decorator

def allure_attributes(description=None, tags=None, severity_level=allure.severity_level.NORMAL, writer=None):
    """
    Decorator to apply Allure description, tags, and severity level to a test function.

    :param description: str
        The description of the test, which appears in the Allure report.
    :param tags: list of str
        A list of tags to label the test. Supports multiple tags.
    :param severity_level: allure.severity_level
        The severity level of the test, levels of severity are: BLOCKER / CRITICAL / NORMAL / MINOR / TRIVIAL
        Set this by using: allure.severity_level.TRIVIAL
    :param writer: str
        The writer of the test

    :return: function
        The wrapped test function with applied Allure metadata.
    """

    def decorator(test_func):
        """
        Inner decorator to wrap the test function and apply the specified Allure metadata.

        :param test_func: function
            The test function to which Allure attributes will be applied.

        :return: function
            The test function wrapped with Allure metadata, prepared for execution.
        """

        test_func._is_attributed = True  # Mark the function as decorated

        @wraps(test_func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function to apply Allure attributes dynamically and execute the test function.

            :param args: list
                Positional arguments passed to the test function.
            :param kwargs: dict
                Keyword arguments passed to the test function.

            :return: Any
                Returns the result of the test function execution.
            """
            # Apply description if provided
            if description:
                allure.dynamic.description(description)

            # Apply tags if provided (supports multiple tags)
            if tags:
                allure.dynamic.tag(*tags)  # Unpack the tags list to allow multiple tags

            # Apply severity level if provided
            allure.dynamic.severity(severity_level)

            if writer:
                allure.dynamic.label("owner", writer)

            # Execute the test function
            return test_func(*args, **kwargs)

        return wrapper

    return decorator


@allure.step("Clicking on element")
def element_click(driver, by_type, finder_value, test_logger, timeout=120):
    """
        Clicks on an element identified by `by_type` and `finder_value` after ensuring it is visible,
        clickable, enabled, and not read-only within the specified timeout.

        :param driver: WebDriver
            The WebDriver instance used for locating elements.
        :param by_type: str
            The type of locator strategy used (e.g., 'id', 'xpath').
        :param finder_value: str
            The value of the locator to find the element.
        :param test_logger: Test logger
        :param timeout: int, optional
            The maximum time in seconds to wait for each condition (default: 120).

        :return: None
            Does not return any value.
    """
    element = element_wait_visible_and_enabled(driver, by_type, finder_value, test_logger, timeout)
    with allure.step(f"Clicking {finder_value}"):
        if element is not None:
            try:
                element.click()
                test_logger.info(f'{finder_value} has been clicked')
            except Exception as e:
                test_logger.error(f'Failed to click on element, failing test')
                pytest.fail(f"Failed to click element: {str(e)}")


@allure.step("Waiting on element")
def element_wait(driver, by_type, finder_value, test_logger, timeout=120):
    """
    Waits for an element identified by `by_type` and `finder_value` to be present
    within the specified timeout.


    :param driver: WebDriver or RemoteWebDriver
        The WebDriver instance used for locating elements.
    :param by_type: str
        The type of locator strategy used (e.g., 'id', 'xpath', 'ANDROID_UIAUTOMATOR').
    :param finder_value: str
        The value of the locator to find the element.
    :param test_logger: Test Logger
    :param timeout: int, optional
        The maximum time in seconds to wait for the element to be present (default: 120).

    :return: WebElement or None
        Returns WebElement if element is found within the timeout.
        Returns None if element is not found or if any exception occurs during the wait.
    """
    wait = WebDriverWait(driver, timeout=timeout)

    # Determine locator based on `by_type`
    if isinstance(driver, webdriver.Remote):  # Appium driver, likely mobile
        test_logger.debug(f'Found Appium call in by_type: {by_type}')
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, finder_value) if by_type == AppiumBy.ANDROID_UIAUTOMATOR else (by_type, finder_value)
    else:
        test_logger.debug(f"Didn't find Appium in by_type, assuming Selenium: {by_type}")
        locator = (by_type, finder_value)

    with allure.step(f"Waiting for {finder_value}"):
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            test_logger.info(f'Element found: {element.text}')
            return element  # Return the element if found
        except Exception as e:
            test_logger.error(f'Could not find "f{finder_value}" in {timeout} seconds: {e}')
            pytest.fail(f"Element not found within the specified time: {str(e)}")


@allure.step("Checking to see if element is clickable")
def element_clickable(driver, by_type, finder_value, timeout=120):
    """
        Waits for an element identified by `by_type` and `finder_value` to be clickable
        within the specified timeout.

        :param driver: WebDriver
            The WebDriver instance used for locating elements.
        :param by_type: str
            The type of locator strategy used (e.g., 'id', 'xpath').
        :param finder_value: str
            The value of the locator to find the element.
        :param timeout: int, optional
            The maximum time in seconds to wait for the element to be clickable (default: 120).

        :return: WebElement or None
            Returns WebElement if element becomes clickable within the timeout.
            Returns None if element does not become clickable or if any exception occurs.

    """
    wait = WebDriverWait(driver, timeout=timeout)
    with allure.step(f"Waiting for {finder_value} to be clickable"):
        try:
            return wait.until(EC.element_to_be_clickable((by_type, finder_value)))
        except Exception as e:
            pytest.fail(f"Element did not become clickable: {str(e)}")

@allure.step("Sending keyboard input to element")
def element_send_keys(driver, by_type, finder_value, keys, test_logger, timeout=120):
    """
        Send keys to an element identified by `by_type` and `finder_value` after ensuring it is visible,
        clickable, enabled, and not read-only within the specified timeout.


        :param driver: WebDriver
            The WebDriver instance used for locating elements.
        :param by_type: str
            The type of locator strategy used (e.g., 'id', 'xpath').
        :param finder_value: str
            The value of the locator to find the element.
        :param keys: str
            The keys to send to the element.
        :param test_logger: Test logger
        :param timeout: int, optional
            The maximum time in seconds to wait for each condition (default: 120).

        :return: None
            Does not return any value.
    """
    element = element_wait_visible_and_enabled(driver, by_type, finder_value, test_logger, timeout)
    test_logger.debug(f'Keys to send: {keys}')
    if element is not None:
        with allure.step(f"Sending {keys} to {finder_value}"):
            try:
                element.send_keys(keys)
                test_logger.info(f'Sending "{keys}" to {finder_value}')
            except Exception as e:
                test_logger.error(f"Failed to sending {keys} to element: {str(e)}")
                pytest.fail(f"Failed to sending {keys} to element: {str(e)}")


@allure.step("Waiting for element to be visible and enabled")
def element_wait_visible_and_enabled(driver, by_type, finder_value, test_logger, timeout=300):
    """
    Wait for an element identified by `by_type` and `finder_value` to become present and enabled
    within the specified timeout, adapting based on driver type (web or mobile).

    :param driver: WebDriver or RemoteWebDriver
        The WebDriver instance to use for locating elements.
    :param by_type: str
        The type of locator strategy to use (e.g., 'id', 'xpath', 'ANDROID_UIAUTOMATOR').
    :param finder_value: str
        The value of the locator to find the element.
    :param test_logger: Test Logger
    :param timeout: int, optional
        The maximum time in seconds to wait for each condition (default: 120).

    :return: WebElement
        Returns WebElement if element is present and enabled.
    """
    wait = WebDriverWait(driver, timeout)

    # Adjust based on driver type
    if isinstance(driver, webdriver.Remote):  # Assuming RemoteWebDriver indicates mobile testing
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, finder_value) if by_type.lower() == 'android_uiautomator' else (
            by_type, finder_value)
        test_logger.debug(f'Found instance of webdriver.remote in driver: {driver}, assuming Selenium locator: {locator}')
    else:
        locator = (by_type, finder_value)
        test_logger.debug(f'Setting Appium locator: {locator}')

    try:
        with allure.step(f"Waiting for {finder_value} to be visible and enabled"):
            element = wait.until(EC.presence_of_element_located(locator))

            # Custom condition for element being enabled (bypassing element_to_be_clickable)
            def is_enabled(driver):
                el = driver.find_element(*locator)
                return el.is_enabled()

            wait.until(is_enabled, f"Element located by {locator} was not enabled within {timeout} seconds")
            test_logger.info(f'Element value after waiting: {element}')
            return element  # Return element if it passes all checks

    except TimeoutException:
        test_logger.error(f'Could not find ({by_type}: {finder_value}) after {timeout} seconds')
        pytest.fail(f"Timeout waiting for element to be present: ({by_type}: {finder_value})")
    except Exception as e:
        test_logger.error(f'({by_type}: {finder_value}) not ready for interaction: {str(e)}')
        pytest.fail(f"Element not ready for interaction: {str(e)}")

@allure.step("Click and holding on element")
def element_click_and_hold(driver, by_type, finder_value, test_logger, x_value=None, y_value=None, original_size=None, timeout=120):
    """
        Clicks and holds on an element identified by `by_type` and `finder_value` after ensuring it is visible,
        clickable, enabled, and not read-only within the specified timeout. Optionally, moves to a specific
        location on the element defined by `x_value` and `y_value`.

        :param driver: WebDriver
            The WebDriver instance used for locating elements.
        :param by_type: str
            The type of locator strategy used (e.g: 'id', 'xpath').
        :param finder_value: str
            The value of the locator to find the element.
        :param test_logger: Test logger
        :param x_value: int or None, optional
            X-coordinate offset on the element to move to (default: None).
        :param y_value: int or None, optional
            Y-coordinate offset on the element to move to (default: None).
        :param original_size: tuple or None, optional
            Original size of the element to calculate new coordinates (default: None).
        :param timeout: int, optional
            The maximum time in seconds to wait for each condition (default: 120).

        :return: WebElement or bool or None
            Returns WebElement if element is found and successfully clicked and held.
            Returns True if element is found, successfully moves to the specified coordinates, and clicks and holds.
            Returns None if any condition times out, element is not found, or if any operation fails.
    """
    element = element_wait_visible_and_enabled(driver, by_type, finder_value, test_logger, timeout)
    actions = ActionChains(driver)
    if x_value and y_value and original_size:
        with allure.step(f"Click and holding on {finder_value}, then moving too X:{x_value} Y:{y_value}"):
            try:
                current_size = driver.get_window_size()
                test_logger.debug(f'Current size of window: {current_size}')
                x_value, y_value = calculate_new_coordinates((x_value, y_value), original_size,
                                                             (current_size['width'], current_size['height']))
                test_logger.debug(f'After calculation: {x_value}x{y_value}')
                actions.move_to_element_with_offset(element, x_value, y_value).click_and_hold().perform()
                return True
            except Exception as e:
                test_logger.error(f'Failed to click and hold at {x_value}x{y_value}: {e}')
                pytest.fail(f"{str(e)}")
                return None
    if element is not None:
        with allure.step(f"Click and holding on {finder_value}"):
            try:
                element = driver.find_element(by_type, finder_value)
                actions.move_to_element(element).click_and_hold().perform()
                test_logger.info(f'Clicked and holding on {finder_value}')
                return element
            except Exception as e:
                test_logger.error(f'Failed to click and hold on {finder_value}: {e}')
                pytest.fail(f"{str(e)}")
                return None
    return None


@allure.step("Release mouse over element")
def element_mouse_up(driver, by_type, finder_value, test_logger, timeout=120):
    """
        Releases the mouse click on an element identified by `by_type` and `finder_value`
        after ensuring it is visible, clickable, enabled, and not read-only within the
        specified timeout.

        :param driver: WebDriver
            The WebDriver instance used for locating elements.
        :param by_type: str
            The type of locator strategy used (e.g., 'id', 'xpath').
        :param finder_value: str
            The value of the locator to find the element.
            :param test_logger: Test logger
        :param timeout: int, optional
            The maximum time in seconds to wait for each condition (default: 120).

        :return: WebElement or None
            Returns WebElement if element is found and mouse click is released successfully.
            Returns None if any condition times out, element is not found, or if releasing the click fails.

    """
    wait = WebDriverWait(driver, timeout)
    element = element_wait_visible_and_enabled(driver, by_type, finder_value, test_logger, timeout)
    if element is not None:
        with allure.step(f"Releasing mouse over {finder_value}"):
            try:
                element = driver.find_element(by_type, finder_value)
                actions = ActionChains(driver)
                actions.move_to_element(element).release().perform()
                test_logger.info(f'Lifted mouse up at: {finder_value}')
                return element
            except Exception as e:
                test_logger.error(f'Failed to lift the mouse up: {e}')
                pytest.fail(f"{str(e)}")
                return None
    return None


@allure.step("Click and dragging")
def element_click_and_drag(driver, elements, test_logger, original_size=None, timeout=120):
    """
        Perform click and drag action on multiple elements, takes optional co-ordinate values.

        :param driver: Driver instance for Selenium or Appium
        :param elements: List of (by_type, finder_value, [x_coord, y_coord]) pairs
        :param test_logger: Test logger
        :param original_size: Original window size (width, height) for co-ordinate recalculation
        :param timeout: Maximum time to wait for elements
        :return: True if operation is successful, False otherwise
    """
    wait = WebDriverWait(driver, timeout)
    actions = ActionChains(driver)

    if not elements:
        return None

    # Handle the first element with click_and_hold
    first_by_type, first_finder_value, *first_coords = elements[0]
    test_logger.info(f'First element: {first_finder_value}')
    first_element = element_wait_visible_and_enabled(driver, first_by_type, first_finder_value, test_logger, timeout)
    if first_element is None:
        test_logger.error(f'First element is none')
        return None
    with allure.step(f"Click and dragging too {elements[0]}"):
        try:
            if first_coords:
                x, y = first_coords[0]
                test_logger.debug(f'x: {x} and y: {y} before conversion')
                current_size = driver.get_window_size()
                test_logger.debug(f'Current window size: {current_size}')
                x, y = calculate_new_coordinates((x, y), original_size, (current_size['width'], current_size['height']))
                test_logger.debug(f'x: {x} and y: {y} after conversion')
                actions.move_to_element_with_offset(first_element, x, y).click_and_hold().perform()
            else:
                element_click_and_hold(driver, first_by_type, first_finder_value, test_logger, timeout)
        except Exception as e:
            test_logger.error(f'Error in click and holding at: {first_finder_value}')
            pytest.fail(f"Error in click_and_hold: {str(e)}")
            return None

    # Handle intermediate elements with move_to_element
    for by_type, finder_value, *coords in elements[1:-1]:
        test_logger.info(f'Moving to: {finder_value}')
        element = element_wait_visible_and_enabled(driver, by_type, finder_value, test_logger, timeout)
        if element is None:
            test_logger.error(f'No element found')
            return None
        try:
            if coords:
                with allure.step(f"Dragging to {coords}"):
                    x, y = coords[0]
                    current_size = driver.get_window_size()
                    test_logger.debug(f'Windows size: {current_size}')
                    x, y = calculate_new_coordinates((x, y), original_size, (current_size['width'], current_size['height']))
                    test_logger.info(f'x: {x} and y: {y}')
                    actions.move_to_element_with_offset(element, x, y).perform()
            else:
                with allure.step(f"Dragging to {finder_value}"):
                    test_logger.debug(f'Dragging to {finder_value}')
                    element_move_to(driver, by_type, finder_value, timeout)
        except Exception as e:
            test_logger.error(f'Failed to move to {finder_value}: {e}')
            pytest.fail(f"Error in move_to_element: {str(e)}")
            return None

    # Handle the last element with release
    last_by_type, last_finder_value, *last_coords = elements[-1]
    test_logger.info(f'Last element: {last_finder_value}')
    last_element = element_wait_visible_and_enabled(driver, last_by_type, last_finder_value, test_logger, timeout)
    if last_element is None:
        test_logger.error(f'Cannot find the last element')
        return None
    try:
        if last_coords:
            with allure.step(f"Dragging to {last_coords} and releasing"):
                x, y = last_coords[0]
                current_size = driver.get_window_size()
                test_logger.debug(f'Windows size: {current_size}')
                x, y = calculate_new_coordinates((x, y), original_size, (current_size['width'], current_size['height']))
                test_logger.info(f'Moving to {x}x{y} and releasing')
                actions.move_to_element_with_offset(last_element, x, y).release().perform()
        else:
            with allure.step(f"Dragging to {last_finder_value} and releasing"):
                element_mouse_up(driver, last_by_type, last_finder_value, test_logger, timeout)
    except Exception as e:
        test_logger.error(f'Error in releasing at {elements}: {e}')
        pytest.fail(f"Error in release: {str(e)}")
        return None
    return True


@allure.step("Moving to element")
def element_move_to(driver, by_type, finder_value, test_logger, timeout=120):
    """
        Moves the mouse cursor to an element identified by `by_type` and `finder_value`
        after ensuring it is visible, clickable, enabled, and not read-only within the
        specified timeout.

        :param driver: WebDriver
            The WebDriver instance used for locating elements.
        :param by_type: str
            The type of locator strategy used (e.g., 'id', 'xpath').
        :param finder_value: str
            The value of the locator to find the element.
        :param test_logger: Test logger
        :param timeout: int, optional
            The maximum time in seconds to wait for each condition (default: 120).

        :return: WebElement or None
            Returns WebElement if element is found and mouse cursor moves to it successfully.
            Returns None if any condition times out, element is not found, or if moving the cursor fails.

        """
    wait = WebDriverWait(driver, timeout)
    element = element_wait_visible_and_enabled(driver, by_type, finder_value, test_logger, timeout)
    if element is not None:
        with allure.step(f"Moving too {finder_value}"):
            try:
                element = driver.find_element(by_type, finder_value)
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                return element
            except Exception as e:
                test_logger.error(f'Error moving to {finder_value}: {e}')
                pytest.fail(f"{str(e)}")
    return None


@allure.step("Getting current window size")
def get_current_size(driver):
    return driver.get_window_size()


@allure.step("Calculating coordinates based on screen size")
def calculate_new_coordinates(original_cords, original_size, current_size):
    """
        Do some maths to change the coordinate values used for clicking items in the design area

        :param original_cords: The coordinate values to change in a (x,y) format
        :param original_size: Size of the Window / device screen when the test was written
        :param current_size: The size of the window / device screen the test is going to run on
        :return: new_x, new_y

        Example:
            calculate_new_coordinates((500,700),(1920,1080),(960,540))
        """
    original_x, original_y = original_cords
    original_width, original_height = original_size
    current_width, current_height = current_size

    new_x = int(original_x * current_width / original_width)
    new_y = int(original_y * current_height / original_height)

    return new_x, new_y
