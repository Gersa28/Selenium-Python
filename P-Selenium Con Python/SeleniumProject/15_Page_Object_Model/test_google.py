import unittest
from selenium import webdriver
from google_page import GooglePage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class GoogleTest(unittest.TestCase):

    @classmethod # Si se agregan nuevos tests correran en una sola instancia del navegador
    def setUpClass(cls):
        """ Test fixture to prepare everything. """
        # Use the ChromeDriverManager to automatically handle the path to chromedriver
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.maximize_window()

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Aws Workshops')

        self.assertEqual('Aws Workshops', google.keyword)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))