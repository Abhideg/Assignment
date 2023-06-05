import openpyxl
import time
import unittest
from selenium import webdriver
from pageobjects.checkoutpage import CheckoutPage
from pageobjects.loginpage import LoginPage
from pageobjects.cartpage import ProductPage
from testdata.checkoutpagedata import CheckoutPageData


class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.ls = LoginPage(self.driver)
        self.ls.complete_login("standard_user", "secret_sauce")
        self.product_page = ProductPage(self.driver)
        self.product_page.get_product_name()
        self.product_page.click_add_to_cart()
        self.product_page.click_cart_icon()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        self.load_data = CheckoutPageData()
        # Load data from Excel file
        data = self.load_data.load_test_data_from_excel("testdata/UserData.xlsx", "Sheet1")

        # Click on Checkout button
        checkout_page = CheckoutPage(self.driver)
        checkout_page.click_checkout_button().click()
        time.sleep(3)

        for row in data:
            # Extract data from each row
            first_name = row["FirstName"]
            last_name = row["LastName"]
            zip_code = row["ZipCode"]

            # Enter personal information
            checkout_page.enter_first_name().send_keys(first_name)
            checkout_page.enter_last_name().send_keys(last_name)
            checkout_page.enter_zip_code().send_keys(zip_code)

            # Click on Continue button
            checkout_page.click_continue_button().click()
            time.sleep(3)

            # Click on Finish button
            checkout_page.click_finish_button().click()
            time.sleep(2)
            # Get the final message
            thank_you_message = checkout_page.get_thank_you_message()

            # Assert the final message
            self.assertEqual(thank_you_message, "Thank you for your order!")


if __name__ == '__main__':
    unittest.main()
