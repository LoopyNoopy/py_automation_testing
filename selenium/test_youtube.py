from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import unittest

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    def tearDown(self) -> None:
        if self.browser:
            self.browser.quit()

    def test_load_trending(self) -> None:
        self.browser.set_window_size(1482, 996)
        self.browser.get("https://www.youtube.com")
        assert "Cake" in self.browser.title
