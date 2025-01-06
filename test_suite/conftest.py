import socket
import pytest
import requests
from appium.options.common import AppiumOptions
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import sys
import time
from collections import defaultdict
import threading
import logging
from datetime import datetime
from appium.webdriver.webdriver import WebDriver as AppiumWebDriver
import allure
import os
import base64


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

file_lock = threading.Lock()

@allure.step("Checking if running on host grid")
def get_ip_address(test_logger = None):
    """
    Gets the IP address of the current machine.

    This function creates a socket connection to determine the IP address of the current machine.

    :return: The IP address as a string, or None if an error occurs.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
    except Exception as e:
        test_logger.error(e)
        ip_address = None
    finally:
        s.close()
    return ip_address


@allure.step("Checking if the grid is reachable")
def is_selenium_grid_reachable(url, timeout=5, test_logger = None):
    """
    Checks if the Selenium Grid URL is reachable.

    This function sends a GET request to the provided URL to determine if the Selenium Grid
    is reachable.

    :param test_logger: Test logger
    :param url: The URL of the Selenium Grid.
    :param timeout: Optional timeout for the request, default is 5 seconds.

    :return: True if the Selenium Grid is reachable, False otherwise.
    """
    with allure.step(f"Checking if we get a status code of 200 from {url}"):
        try:
            response = requests.get(url, timeout=timeout)
            #data = response.json(#or data.get('value', {}).get('ready') == True
            if response.status_code == 200:
                test_logger.debug(f'{url} is reachable')
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            test_logger.warning(f'Error connecting to {url}: {e}')
            return False


@allure.step("Checking if caps are supported")
def is_capability_supported(grid_url, capabilities, test_logger):
    """
    Checks if the Selenium Grid supports the requested capabilities.

    This function queries the Selenium Grid at the provided `grid_url` for its current status,
    and verifies if it has nodes that are ready and capable of handling the specified capabilities.
    The comparison between the node's capabilities and the requested ones is done in a
    case-insensitive manner.

    :param grid_url: URL of the Selenium Grid to check.
    :param capabilities: Dictionary containing the desired capabilities to check against the grid's nodes.
    :param test_logger: Test logger

    :return: Boolean value indicating whether the grid supports the requested capabilities.

    :raises None: Handles connection errors internally by returning False.
    """
    try:
        with allure.step(f"Getting the reported status from {grid_url}"):
            response = requests.get(f"{grid_url}/status")
            response.raise_for_status()
            grid_status = response.json()

            # Log the status response for debugging
            test_logger.debug(f'Response from {grid_url}: {grid_status}')

        with allure.step(f"Checking to see if the grid is ready"):
            if not grid_status.get('value', {}).get('ready', False):
                test_logger.warning(f"Grid at {grid_url} is not ready")
                return False

        with allure.step(f"Checking to see if there is a node that supports the capabilities"):
            nodes = grid_status.get('value', {}).get('nodes', [])
            for node in nodes:
                for slot in node.get('slots', []):
                    stereotype = slot.get('stereotype', {})

                    # Convert keys to lowercase for case-insensitive comparison
                    capabilities_lower = {key.lower(): value for key, value in capabilities.items()}
                    stereotype_lower = {key.lower(): value for key, value in stereotype.items()}

                    # Debug: Print capabilities and stereotype
                    #print("Requested capabilities (lowercase):", capabilities_lower)
                    #print("Node's capabilities (lowercase):", stereotype_lower)

                    # Check if node's capabilities (stereotype) are a subset of requested capabilities
                    match = True
                    for key, value in stereotype_lower.items():
                        if capabilities_lower.get(key) != value and value != 'ANY':
                            match = False
                            #print(
                            #    f"Mismatch found for key '{key}': node value '{value}' != requested value '{capabilities_lower.get(key)}'")
                            break
                    if match:
                        return True

        test_logger.warning(f"Capabilities {capabilities} are not supported by grid at {grid_url}")
        return False

    except requests.exceptions.RequestException as e:
        test_logger.error(f"Error connecting to Selenium Grid: {e}")
        return False


@allure.step("Checking if caps are for Appium")
def is_appium_capabilities(caps):
    return any(key.startswith("appium:") for key in caps)


@allure.step("Finding Grid that supports caps")
def which_grid(caps, test_logger):
    """
    Determines the appropriate Selenium Grid URL to use based on availability and supported capabilities.

    This function attempts to connect to a local or LAN-based Selenium Grid and checks if it supports
    the specified capabilities. It returns the URL of the grid that can fulfill the request.

    :param caps: Dictionary containing the desired capabilities for the Selenium Grid.
    :param test_logger: Test logger

    :return: URL of the Selenium Grid that supports the specified capabilities.

    :raises Exception: If no available grid supports the desired capabilities.
    """

    with allure.step(f"Figuring out which URLS to try and connect too"):
        # Figuring out how to connect to lan grid
        if get_ip_address(test_logger) == "Mekhane.local":
            lan_grid_url = 'http://localhost:4444'
            test_logger.info(f'Running on Mekhane, changing lan grid to {lan_grid_url}')
        else:
            lan_grid_url = 'http://Mekhane.local:4444'
            test_logger.info(f'Not running on Mekhane, changing lan grid to {lan_grid_url}')

        #lan_grid_url = 'http://192.168.122.64:4444'
        local_grid_url = "http://localhost:4444"
        appium_local_url = "http://localhost:4723/status"

        # List of grid URLs to check along with a flag for whether to check capabilities
        test_logger.debug(f'Local Grid: {local_grid_url} / Lan grid: {lan_grid_url}')
        grid_urls = [
            (local_grid_url, True),
            (lan_grid_url, True),
        ]

        # If the caps contain Appium capabilities, add appium_local_url to the list of URLs to check
        if is_appium_capabilities(caps):
            grid_urls.append((appium_local_url, False))  # Do not check capabilities for appium_local_url

    # Iterate through the URLs and check if the grid is reachable and optionally supports the capabilities
    for url, check_capabilities in grid_urls:
        with allure.step(f"Checking to see if {url} is usable"):
            if is_selenium_grid_reachable(url,test_logger = test_logger):
                if not check_capabilities or is_capability_supported(url, caps, test_logger):
                    # If we're using the local Appium server, check device availability
                    if url == appium_local_url:
                        if wait_for_device_availability(url):  # Wait if the device is busy
                            return "http://localhost:4723"
                        else:
                            raise Exception("Local Appium server device is busy or unavailable.")
                    return url

    # If no grid supports the desired capabilities, raise an exception
    test_logger.error("No grid supports the desired capabilities")
    raise Exception("No grid supports the desired capabilities")


@allure.step("Checking if local appium server is busy")
def wait_for_device_availability(command_executor, timeout=300, interval=10):
    """
    Waits for a device to become available on the Appium server by polling the `/status` endpoint.

    :param command_executor: The Appium server URL (command executor).
    :param timeout: Maximum time (in seconds) to wait for the device to become available.
    :param interval: Time interval (in seconds) between each availability check.
    :return: True if the device becomes available within the timeout, False otherwise.
    """
    with allure.step(f"Waiting {timeout} seconds for the device to be ready"):
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                response = requests.get(f"{command_executor}/status")
                response_json = response.json()
                # Check if there's an active session on the Appium server
                if response_json.get("value", {}).get("sessionId") is None:
                    # No active session, device is available
                    return True
                else:
                    print("Device is busy, waiting for it to become available...")
            except requests.exceptions.RequestException as e:
                print(f"Failed to connect to Appium server: {e}")
            time.sleep(interval)
        return False


def pytest_addoption(parser):
    """
    Add custom command-line options to the pytest parser.

    :param parser: The argument parser for command-line options.
    """
    parser.addoption("--apk_path", action="store", default=None,
                     help="Path to the APK file for Android Devices")
    parser.addoption("--ipa_path", action="store", default=None,
                     help="Path to the IPA file to run on iOS devices")
    parser.addoption("--web_url", action="store", default=None,
                     help="URL to Silhouette Web")
    parser.addoption("--msix_path", action="store", default=None,
                     help="Path to the MSIX file for windows desktop apps")
    parser.addoption("--pkg_path", action="store", default=None,
                     help="Path to the .pkg file for macOS apps")
    parser.addoption("--exe_path", action="store", default=None,
                     help="Path to the exe file for windows desktop apps")
    parser.addoption("--dmg_path", action="store", default=None,
                     help="Path to the dmg file for macOS desktop apps")
    parser.addoption("--version_no", action="store", default=None,
                     help="Version number of the app being tested")
    parser.addoption("--device_name", action="store", default=None,
                     help="Name of devices you want the tests to run on")


@allure.story("Provides the path to the APK of Silhouette Go")
@pytest.fixture(scope="session")
def apk_path(request):
    """
    Fixture to provide the APK file path for Android devices.

    :param request: The fixture request object.

    :return: str path to the APK file.
    """
    return request.config.getoption("--apk_path")


@allure.story("Provides the path to the IPA of Silhouette Go")
@pytest.fixture(scope="session")
def ipa_path(request):
    """
    Fixture to provide the IPA file path for iOS devices.

    :param request: The fixture request object.

    :return: str path to the IPA file.
    """
    return request.config.getoption("--ipa_path")


@allure.step("Return what URL to test Silhouette Web")
@pytest.fixture(scope="session")
def web_url(request):
    """
    Fixture to provide the URL to the Silhouette Web.

    :param request: The fixture request object.

    :return: str URL to Silhouette Web.
    """
    return request.config.getoption("--web_url")


@allure.step("Return the version number being sent")
@pytest.fixture(scope="session")
def version_no(request):
    """
    Fixture to provide the version number of the app being tested.

    :param request: The fixture request object.

    :return: str Version number of the app.
    """
    return request.config.getoption("--version_no")


@pytest.fixture(scope="session")
def android_device(request):
    """
    Fixture to provide the name of the Android device for testing.

    :param request: The fixture request object.

    :return: str Name of the Android device.
    """
    return request.config.getoption("--android_device")


@pytest.fixture(scope="session")
def android_version(request):
    """
    Fixture to provide the Android version for testing.

    :param request: The fixture request object.

    :return: str Android version.
    """
    return request.config.getoption("--android_version")


@pytest.fixture(scope="session")
def device_name_local(request):
    """
    Fixture to provide the name of the devices for testing.

    :param request: The fixture request object.

    :return: str Name of the devices.
    """
    return request.config.getoption("--device_name")


@allure.step("Setting which device to use")
@pytest.fixture(params=[
    ('ANDROID', None, '14', 'UiAutomator2'),
    ('ANDROID', None, '13', 'UIAutomator2')
    #('ANDROID', None, '12', 'UIAutomator2')
    #('ANDROID', None, '11', 'UIAutomator2')
    #('iOS', None, '17', 'XCUITest'),
    #('iOS', None, '16', 'XCUITest'),
    #('iOS', None, '15', 'XCUITest')
], ids=lambda param: f"{param[0]} - {param[2]} ")
def device_info(request):
    """
    Fixture to provide device information for mobile testing.

    :param request: The fixture request object.

    :return: Tuple containing platform, device name, version, and mobile driver name.
    """
    return request.param


@allure.step("Setting which operating system to use")
@pytest.fixture(params=[
    'Windows 10',
    'Windows 11',
    'mac'
], ids=lambda param: f" {param} ")
def os_info(request):
    """
    Fixture to provide the operating system information for testing.

    This fixture parameterizes tests with different operating systems, allowing tests to be run
    across multiple OS environments, such as 'Windows 10', 'Windows 11', and 'mac'.

    :param request: The fixture request object from pytest.

    :return: str representing the operating system being tested.
    """
    return request.param

@allure.step("Setting which browser to use and version")
@pytest.fixture(params=[
    #('chrome', ChromeOptions(), 'stable'),
    ('chrome', ChromeOptions()),  # Temp until we can get different versions of Chrome on nodes
    #('chrome', ChromeOptions(), 'beta'),
    #('chrome', ChromeOptions(), 'dev'),
    #('chrome', ChromeOptions(), 'canary'),
    #('chrome', ChromeOptions(), 'nightly'),
    #('firefox', FirefoxOptions(), 'esr'),
    ('firefox', FirefoxOptions()),  # Temp until we can get different versions of firefox on nodes
    #('firefox', FirefoxOptions(), 'latest'),
    #('firefox', FirefoxOptions(), 'beta'),
    #('firefox', FirefoxOptions(), 'dev')
], ids=lambda param: f"{param[0]} - {param[2]}" if len(param) == 3 else f"{param[0]} ({param[1].__class__.__name__})")
def browser_info(request):
    """
    Fixture to provide browser information for testing across different versions.

    This fixture parameterizes tests with different browser names and versions, allowing them to
    be run on different browser configurations, such as 'Chrome', 'Firefox', and their various versions
    (stable, beta, dev, etc.).

    :param request: The fixture request object from pytest.

    :return: Tuple containing the browser name, browser options, and an optional version string.
    """
    return request.param


@allure.step("Setting window size")
@pytest.fixture(scope="function", params=[
    (1920, 1080),  # Full HD - Common on desktops and laptops
    (1366, 768),   # HD - Common on laptops
    (1536, 864),   # HD+ - Common on laptops
    (1440, 900),   # WXGA+ - Common on older laptops
    (1600, 900),   # HD+ - Common on laptops and desktops
    (2560, 1440),  # QHD - Common on high-end desktops
    (3840, 2160),  # 4K UHD - High-end desktops and TVs
    (1280, 720),   # HD - Common on smaller devices and laptops
    (2340, 1080),  # FHD+ - Common on newer high-resolution mobile devices
    (2736, 1824)   # Surface Pro - Popular among high-resolution 2-in-1 devices
], ids=lambda param: f"{param[0]}x{param[1]}")
def window_size(request):
    """
    Fixture to provide the 10 most popular landscape window sizes for testing.

    This fixture parameterizes tests with a variety of popular screen resolutions, simulating different
    screen environments to test responsive design and layout behavior.

    :param request: The fixture request object from pytest.

    :return: Tuple containing the width and height of the window size.
    """
    return request.param


@allure.step("Configuring Mobile Driver")
@pytest.fixture(scope="function")
def mobile_driver(request, device_info, apk_path, ipa_path, version_no, device_name_local, test_logger):
    """
    Pytest fixture to set up and tear down a mobile WebDriver session for mobile app testing.

    :return: Appium WebDriver instance for mobile testing.
    """
    test_name = request.node.name
    test_logger.info(f'Device info: {device_info}')
    device_platform, device_name, device_version, device_mobile_driver = device_info

    with allure.step("Adding environment variables"):
        allure_dir = request.config.getoption('--alluredir')
        if allure_dir:
            append_to_environment_file("Mobile_OS", f'{device_platform} {device_version}', allure_dir)

    with allure.step("Configuring Mobile Driver"):
        options = AppiumOptions()
        caps = {
            'platformName': device_platform,
            'appium:devicename': device_name,
            'appium:app': apk_path,
            'appPackage': 'com.SilhouetteSoftware.SilhouetteGo',
            'appActivity': 'crc64a817c78ca7edff55.SplashActivity',
            'appium:platformVersion': device_version,
            'appium:automationName': device_mobile_driver,
            'appium:ensureWebviewsHavePages': True,
            'appium:nativeWebScreenshot': True,
            'appium:newCommandTimeout': 120,
            'appium:connectHardwareKeyboard': True,
            'appium:fullReset': True,
        }
        options.load_capabilities(caps)

        # Initialize Appium WebDriver
        mobile_driver = AppiumWebDriver(command_executor=which_grid(caps, test_logger), options=options)

    # Start recording the screen
    mobile_driver.start_recording_screen()

    yield mobile_driver

    # Teardown
    if mobile_driver is not None:
        # Stop recording and save video
        video_data = mobile_driver.stop_recording_screen()
        video_file = f"{test_name}.mp4"
        with open(video_file, "wb") as f:
            f.write(base64.b64decode(video_data))
        allure.attach.file(video_file, name="Test Video", attachment_type=allure.attachment_type.MP4)
        os.remove(video_file)  # Cleanup after attaching

        with allure.step("Taking final screenshot and quitting driver"):
            test_logger.debug(f'Checking / creating screenshot folder')
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
            test_logger.debug(f'Saving screenshot at: {screenshot_path} and attaching to report')
            mobile_driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="End of Test", attachment_type=allure.attachment_type.PNG)
            mobile_driver.quit()


@allure.step("Configuring web driver")
@pytest.fixture(scope="function")
def web_driver(request, browser_info, os_info, web_url, window_size, test_logger):
    """
    Pytest fixture to set up and tear down a WebDriver session for browser testing.

    This fixture initializes a WebDriver instance based on provided browser information,
    navigates to a specified URL, and handles cleanup after each test.
    """
    browser_name, browser_options, *version = browser_info
    version = version[0] if version else None
    test_name = request.node.name
    platform = os_info
    test_logger.info(f'Setting up web driver with: browser: {browser_name} / OS: {os_info}')

    session_name = f"{test_name} [{browser_name} on {platform}]"

    # Collect dynamic environment data
    with allure.step("Adding environment variables"):
        allure_dir = request.config.getoption('--alluredir')
        if allure_dir:
            test_logger.info(f'Setting environment variables: {browser_name} {platform} {web_url}')
            append_to_environment_file("Browsers",browser_name,allure_dir)
            append_to_environment_file("Platform",platform,allure_dir)
            append_to_environment_file("Web_URL",web_url,allure_dir)

    with allure.step("Configuring Web Driver"):
        test_logger.info(f'Setting capabilities')
        browser_options.set_capability('browserName', browser_name)
        browser_options.set_capability('platformName', platform)

        if browser_name == 'chrome' and version:
            browser_options.set_capability('browserVersion', version)
        elif browser_name == 'firefox' and version:
            browser_options.set_capability('browserVersion', version)

        capabilities = browser_options.to_capabilities()
        test_logger.info("Setting up web driver")
        driver = webdriver.Remote(
            command_executor=f'{which_grid(capabilities, test_logger)}',
            options=browser_options
        )

        # Set window size
        test_logger.info(f'Setting window size to {window_size}')
        driver.set_window_size(window_size[0], window_size[1])

        test_logger.info("Launching driver")
        driver.get(web_url)

    yield driver

    # Clean up and take a screenshot
    if driver is not None:
        with allure.step("Taking final screenshot and quiting driver"):
            test_logger.debug(f'Checking / creating screenshot folder')
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
            test_logger.debug(f'Saving screenshot at: {screenshot_path} and attaching to report')
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="End of Test", attachment_type=allure.attachment_type.PNG)
            driver.quit()


@pytest.fixture(scope="function")
def eyes():
    """
    Pytest fixture to initialize and tear down Applitools Eyes for visual testing.

    This fixture sets up an Applitools Eyes instance and closes it after the test completes.

    :return: Eyes instance for visual testing.
    """
    eyes = Eyes()
    eyes.api_key = 'KW49ib7XoFI0CnzOpLKxDOE11U6CDif1gV7Y6Ujd7rs110'
    yield eyes
    eyes.close()


def pytest_runtest_setup(item):
    # Check if the test function has the `_is_decorated` attribute
    if not getattr(item.function, "_is_suited", False):
        pytest.fail(f"The test '{item.name}' must be decorated with @allure_suite to specify Allure suite information.")
    if not getattr(item.function, "_is_storied", False):
        pytest.fail(f"The test '{item.name}' must be decorated with @allure_story to specify Allure story information.")
    if not getattr(item.function, "_is_attributed", False):
        pytest.fail(f"The test '{item.name}' must be decorated with @allure_story to specify Allure story information.")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    allure_dir = config.getoption('--alluredir')
    if allure_dir:
        os.makedirs(allure_dir, exist_ok=True)
        env_file = os.path.join(allure_dir, 'environment.properties')
        with open(env_file, 'w') as f:
            f.write("Test_Framework=pytest")


@pytest.hookimpl
def pytest_unconfigure(config):
    """
    Merge worker-specific environment.properties files into a single file and delete them.
    """
    allure_dir = config.getoption('--alluredir')
    if allure_dir:
        final_env_file = os.path.join(allure_dir, 'environment.properties')
        worker_files = [
            os.path.join(allure_dir, f)
            for f in os.listdir(allure_dir)
            if f.startswith('environment_') and f.endswith('.properties')
        ]

        merged_data = {}
        # Merge all worker files into `merged_data`
        for worker_file in worker_files:
            with open(worker_file, 'r') as f:
                for line in f:
                    if '=' not in line.strip():
                        continue
                    k, v = line.strip().split('=', 1)
                    if k in merged_data:
                        existing_values = set(merged_data[k].split(', '))
                        existing_values.update(v.split(', '))
                        merged_data[k] = ', '.join(sorted(existing_values))
                    else:
                        merged_data[k] = v

        # Write the merged data to the final environment.properties file
        with open(final_env_file, 'w') as f:
            for k, v in merged_data.items():
                f.write(f"{k}={v}\n")

        # Ensure all files are processed before deletion
        if os.getenv("PYTEST_XDIST_WORKER") is None:  # Main process only
            for worker_file in worker_files:
                try:
                    os.remove(worker_file)
                except OSError as e:
                    print(f"Error deleting file {worker_file}: {e}")


def append_to_environment_file(key, value, allure_dir):
    """
    Append a key-value pair to a worker-specific environment.properties file.
    If the key already exists, merge the values with a comma separator.
    """
    worker_id = os.getenv("PYTEST_XDIST_WORKER", "default")  # Get worker ID
    env_file = os.path.join(allure_dir, f'environment_{worker_id}.properties')

    with file_lock:
        existing_data = {}
        if os.path.exists(env_file):
            with open(env_file, 'r') as f:
                for line in f:
                    if '=' not in line.strip():
                        continue
                    k, v = line.strip().split('=', 1)
                    existing_data[k] = v

        if key in existing_data:
            existing_values = set(existing_data[key].split(', '))
            existing_values.add(value)
            existing_data[key] = ', '.join(sorted(existing_values))
        else:
            existing_data[key] = value

        with open(env_file, 'w') as f:
            for k, v in existing_data.items():
                f.write(f"{k}={v}\n")


class AllureLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        self.memory_handler = None  # Will be set during logger configuration

    def _attach_to_allure(self, level, message):
        color_map = {
            "DEBUG": "gray",
            "INFO": "green",
            "WARNING": "orange",
            "ERROR": "red",
            "CRITICAL": "darkred",
        }
        color = color_map.get(level, "black")
        styled_message = f'<span style="color:{color};"><strong>{level}:</strong> {message}</span>'
        allure.attach(
            styled_message,
            name=f"{level} Log",
            attachment_type=allure.attachment_type.HTML,
        )


class InMemoryLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.logs = {
            "DEBUG": [],
            "INFO": [],
            "WARNING": [],
            "ERROR": [],
            "CRITICAL": [],
        }
        # Create a formatter with a specific date format
        self.formatter = logging.Formatter(
            fmt="%(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

    def emit(self, record):
        message = self.format(record)
        log_entry = {
            "name": record.name,
            "filename": record.filename,
            "lineno": record.lineno,
            "message": message,
            "time": datetime.fromtimestamp(record.created),  # Store as datetime for sorting
        }
        self.logs[record.levelname].append(log_entry)

    def get_combined_logs_with_colors(self, levels):
        """
        Combine logs from specified levels into a single HTML-styled string with colors,
        sorted by timestamp.
        """
        color_map = {
            "DEBUG": "gray",
            "INFO": "green",
            "WARNING": "orange",
            "ERROR": "red",
            "CRITICAL": "darkred",
        }

        # Merge logs from specified levels into a single list
        all_logs = []
        for level in levels:
            for record in self.logs[level]:
                # Add the level name to each record
                record["level"] = level
                all_logs.append(record)

        # Sort the merged logs by timestamp
        all_logs.sort(key=lambda x: x["time"])

        # Format logs with colors
        combined = []
        for record in all_logs:
            color = color_map.get(record["level"], "black")
            styled_message = (
                f'<span style="color:{color};">'
                f"<strong>[{record['level']}]</strong> {record['name']}:{record['filename']}:{record['lineno']} - "
                f"{record['message']} ({record['time']})"
                f"</span>"
            )
            combined.append(styled_message)

        return "<br>".join(combined)


@pytest.fixture(scope="function")
def test_logger(request):
    test_name = request.node.name
    logging.setLoggerClass(AllureLogger)
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.DEBUG)

    memory_handler = InMemoryLogHandler()
    formatter = logging.Formatter("%(message)s")
    memory_handler.setFormatter(formatter)
    logger.addHandler(memory_handler)
    logger.memory_handler = memory_handler

    stderr_handler = logging.StreamHandler()
    stderr_handler.setLevel(logging.WARNING)
    stderr_handler.setFormatter(formatter)
    logger.addHandler(stderr_handler)

    return logger


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_teardown(item):
    outcome = yield
    logger_name = f"{item.name}"
    logger = logging.getLogger(logger_name)
    memory_handler = getattr(logger, "memory_handler", None)
    if memory_handler:
        # Check for CRITICAL logs
        if memory_handler.logs["CRITICAL"]:
            crit_log = memory_handler.get_combined_logs_with_colors(
                ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
            )
            allure.attach(
                crit_log,
                name=f"Critical Log for {item.name}",
                attachment_type=allure.attachment_type.HTML,
            )

        # Check for ERROR logs
        if memory_handler.logs["ERROR"]:
            error_log = memory_handler.get_combined_logs_with_colors(
                ["DEBUG", "INFO", "WARNING", "ERROR"]
            )
            allure.attach(
                error_log,
                name=f"Error Log for {item.name}",
                attachment_type=allure.attachment_type.HTML,
            )

        # Check for WARNING logs
        if memory_handler.logs["WARNING"]:
            warnings = memory_handler.get_combined_logs_with_colors(
                ["WARNING"]
            )
            allure.attach(
                warnings,
                name=f"Warnings for {item.name}",
                attachment_type=allure.attachment_type.HTML,
            )

        # Check for DEBUG/INFO logs
        if memory_handler.logs["DEBUG"] or memory_handler.logs["INFO"]:
            debug_n_info = memory_handler.get_combined_logs_with_colors(
                ["DEBUG", "INFO"]
            )
            allure.attach(
                debug_n_info,
                name=f"Info Log for {item.name}",
                attachment_type=allure.attachment_type.HTML,
            )
