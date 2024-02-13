from appium.options.common import AppiumOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from appium import webdriver
import pytest
import socket


def get_ip_address():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to a remote server (doesn't actually send any data)
        s.connect(('8.8.8.8', 80))

        # Get the local IP address
        ip_address = s.getsockname()[0]
    except Exception as e:
        print("Error:", e)
        ip_address = None
    finally:
        # Close the socket
        s.close()

    return ip_address


def pytest_addoption(parser):  # If you change these, change the ones in Rabbit_Sender too
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


@pytest.fixture(scope="session")
def apk_path(request):
    return request.config.getoption("--apk_path")


@pytest.fixture(scope="session")
def version_no(request):
    return request.config.getoption("--version_no")


@pytest.fixture(scope="session")
def ipa_path(request):
    return request.config.getoption("--ipa_path")


@pytest.fixture(scope="session")
def android_device(request):
    return request.config.getoption("--android_device")


@pytest.fixture(scope="session")
def android_version(request):
    return request.config.getoption("--android_version")


@pytest.fixture(scope="session")
def device_name_local(request):
    return request.config.getoption("--device_name")


# Set mobile devices: OS / Name / Version / Automation Driver
@pytest.fixture(params=[
    ('Android', None, '11.0', 'UiAutomator2'),
    ('Android', None, '8.1', 'UiAutomator2')
], ids=lambda param: f"{param[1]} - {param[2]} ")
def device_info(request):
    return request.param


# Parameterize orientation of device
@pytest.fixture(params=[
    'PORTRAIT',
    'LANDSCAPE',
], ids=lambda param: f"{param}")
def device_orientation(request):
    return request.param


# ToDo - Find a way to change the platformName on the grid nodes so we can specify what version of macOS we want to
#  test on (Or see if SauceLabs resolves this)
@pytest.fixture(params=[
    'Windows 11',
    'mac'
], ids=lambda param: f"{param} ")
def os_info(request):
    return request.param


# Set browsers to test on: Browser name / Browser Options
@pytest.fixture(params=[
    ('chrome', ChromeOptions()),
    ('firefox', FirefoxOptions()),
    ('edge', EdgeOptions())
], ids=lambda param: f"{param[0]}")
def browser_info(request):
    return request.param


@pytest.fixture(scope="function")
def mobile_driver(request, device_info, device_orientation, apk_path, ipa_path, version_no, device_name_local):
    test_name = request.node.name
    device_platform, device_name, device_version, device_mobile_driver = device_info
    orientation = device_orientation
    options = AppiumOptions()
    caps = {
        'platformName': device_platform,
        # 'appium:deviceName': device_name,
        'appium:app': apk_path,
        'appPackage': '',
        'appActivity': '',
        'appium:platformVersion': device_version,
        'appium:automationName': device_mobile_driver,
        'appium:ensureWebviewsHavePages': True,
        'appium:nativeWebScreenshot': True,
        'appium:newCommandTimeout': 3600,
        'appium:connectHardwareKeyboard': True,
        'appium:fullReset': True
    }
    if device_name:
        caps['appium:deviceName'] = device_name
    options.load_capabilities(caps)
    if get_ip_address() == "":
        url = ''
    else:
        url = ''
    mobile_driver = webdriver.Remote(command_executor=url, options=options)
    mobile_driver.orientation = orientation
    # Yield the mobile_driver to the test
    yield mobile_driver

    # Teardown/Cleanup: Perform actions after the test is done
    if mobile_driver is not None:
        mobile_driver.quit()


@pytest.fixture(scope="function")
def web_driver(request, browser_info, os_info):
    browser_name, browser_options = browser_info
    platform = os_info
    if browser_options:
        browser_options.add_argument(f"browserName:{browser_name}")
        browser_options.platform_name = platform

    # Use webdriver.Remote with capabilities and options
    driver = webdriver.Remote(
        command_executor='',
        options=browser_options
    )
    driver.get('')
    yield driver
    driver.quit()


def browser_test():
    options = ChromeOptions()
    options.set_capability("platformVersion", "14")
    return
