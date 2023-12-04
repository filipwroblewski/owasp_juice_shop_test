import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class JuiceShopTest(unittest.TestCase):
    URL = "https://juice-shop.exemplary.pl/"
    URL = "https://juice-shop.herokuapp.com/#/"

    TEMP_USERNAME = "admin@juice-sh.op"
    TEMP_PASSWORD = "admin123"

    def setUp(self):
        # self.driver = webdriver.Remote(
        #     command_executor="http://selenium-hub:4444/wd/hub",
        #     desired_capabilities={"browserName": "chrome"}
        # )

        serv_obj = Service('./chromedriver/chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=serv_obj, options=options)
        self.driver.maximize_window()

    def test_juice_shop_title(self):
        self.driver.get(self.URL)
        expected_title = "OWASP Juice Shop"
        self.assertIn(expected_title, self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()