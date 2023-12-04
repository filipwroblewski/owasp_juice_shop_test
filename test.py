import unittest
from selenium import webdriver

class JuiceShopTest(unittest.TestCase):
    URL = "https://juice-shop.exemplary.pl/"

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            desired_capabilities={"browserName": "chrome"}
        )

    def test_juice_shop_title(self):
        self.driver.get(self.URL)
        expected_title = "OWASP Juice Shop"
        self.assertIn(expected_title, self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()