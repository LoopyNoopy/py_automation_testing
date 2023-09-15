import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import webdriver_manager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os

os.environ['GH_TOKEN'] = "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"

def test_youtube_home(get_chrome_version_folder,get_chromedriver_version_folder, get_firefox_version_folder):
    custom_chrome_options = webdriver.ChromeOptions()
    custom_chrome_options.binary_location = "chrome\\" + str(get_chrome_version_folder)  +"\\chrome-win64\\chrome.exe"
    chrome_service = Service(executable_path="chromedriver\\"+ str(get_chromedriver_version_folder)  +"\\chromedriver-win64\\chromedriver.exe")
    chrome_driver = webdriver.Chrome(service=chrome_service, options=custom_chrome_options)
    chrome_driver.get("https://www.youtube.com")
    assert chrome_driver.title == "YouTube"
    chrome_driver.quit()

    gecko_driver_path = GeckoDriverManager().install()
    firefox_binary = "firefox\\" + str(get_firefox_version_folder)  +"\\firefox.exe"
    os.environ['PATH'] = f'{os.environ["PATH"]}:{os.path.dirname(gecko_driver_path)}'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = firefox_binary
    firefox_driver = webdriver.Firefox(options=firefox_options)
    firefox_driver.get("https://www.youtube.com")
    assert firefox_driver.title == "YouTube"
    firefox_driver.close()

    return

def test_youtube_trending(get_chrome_version_folder,get_chromedriver_version_folder, get_firefox_version_folder):
    custom_chrome_options = webdriver.ChromeOptions()
    custom_chrome_options.binary_location = "chrome\\" + str(get_chrome_version_folder)  +"\\chrome-win64\\chrome.exe"
    chrome_service = Service(executable_path="chromedriver\\"+ str(get_chromedriver_version_folder)  +"\\chromedriver-win64\\chromedriver.exe")
    chrome_driver = webdriver.Chrome(service=chrome_service, options=custom_chrome_options)
    chrome_driver.get("https://www.youtube.com/feed/trending")
    assert chrome_driver.title == "Trending"
    chrome_driver.quit()

    gecko_driver_path = GeckoDriverManager().install()
    firefox_binary = "firefox\\" + str(get_firefox_version_folder)  +"\\firefox.exe"
    os.environ['PATH'] = f'{os.environ["PATH"]}:{os.path.dirname(gecko_driver_path)}'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = firefox_binary
    firefox_driver = webdriver.Firefox(options=firefox_options)
    firefox_driver.get("https://www.youtube.com/feed/trending")
    assert firefox_driver.title == "Trending"
    firefox_driver.close()

    return