import os
import pytest
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.loginpage import LoginPage
from utilities.customLogger import LogGen


class TestLogin(unittest.TestCase):

    @pytest.mark.regression
    def setUp(self):
        self.logger = LogGen.loggen()
        self.driver = webdriver.Chrome()
        self.logger.info("*************** Test_001_Login *****************")
        self.driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.driver.get("https://www.saucedemo.com/")
        self.ls = LoginPage(self.driver)

    def save_screenshot(self, name):
        screenshots_dir = "reports"
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

    def test_login_locked(self):
        self.logger.info("started complete login test")
        self.ls.complete_login("locked_out_user", "secret_sauce")

        act_lock = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
        expected_lock = "Epic sadface: Sorry, this user has been locked out."
        self.assertEqual(act_lock, expected_lock, f"Actual: {act_lock}, Expected: {expected_lock}")
        if act_lock != expected_lock:
            self.save_screenshot("test_login_locked")

    def test_login_pass(self):
        self.logger.info("started pass test")
        self.ls.complete_login("standard_user", "secret_sauce")

        act_logo = self.driver.find_element(By.XPATH, '//*[@class="app_logo"]').text
        expected_logo = "Swag Labs"
        self.assertEqual(act_logo, expected_logo, f"Actual: {act_logo}, Expected: {expected_logo}")
        if act_logo != expected_logo:
            self.save_screenshot("test_login_pass")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
