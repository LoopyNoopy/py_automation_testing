import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Install GeckoDriver and get its path
gecko_driver_path = GeckoDriverManager().install()

# Specify the path to the Firefox binary
firefox_binary = "firefox\\win64-119.0a1\\firefox.exe"

# Set the environment variable for GeckoDriver
os.environ['PATH'] = f'{os.environ["PATH"]}:{os.path.dirname(gecko_driver_path)}'

# Set up Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = firefox_binary

# Create a Firefox WebDriver instance
firefox_driver = webdriver.Firefox(options=firefox_options)

# Navigate to a website
firefox_driver.get("https://www.youtube.com")

# Close the browser
firefox_driver.quit()
