import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

def test_youtube_trending(get_chrome_version_folder,get_chromedriver_version_folder):
    custom_chrome_options = webdriver.ChromeOptions()
    custom_chrome_options.binary_location = "chrome\\" + str(get_chrome_version_folder)  +"\\chrome-win64\\chrome.exe"
    chrome_service = Service(executable_path="chromedriver\\"+ str(get_chromedriver_version_folder)  +"\\chromedriver-win64\\chromedriver.exe")
    chrome_driver = webdriver.Chrome(service=chrome_service, options=custom_chrome_options)
    chrome_driver.get("https://www.youtube.com")
    chrome_driver.quit()
    return