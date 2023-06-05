import time

import pytest
from selenium import webdriver
from pageobjects.cartpage import ProductPage
from pageobjects.loginpage import LoginPage


@pytest.mark.regression
class TestAddToCart:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.ls = LoginPage(self.driver)
        self.ls.complete_login("standard_user", "secret_sauce")
        self.product_page = ProductPage(self.driver)

    def test_add_to_cart(self):
        # Get the product name
        product_name = self.product_page.get_product_name()

        # Click on "Add to Cart" button
        self.product_page.click_add_to_cart()
        time.sleep(5)
        # Click on cart icon
        self.product_page.click_cart_icon()
        time.sleep(5)
        # Get the products in the cart
        cart_items = self.product_page.get_cart_items()

        # Assert if the added product is in the cart
        assert product_name in cart_items

    def teardown_method(self):
        self.driver.quit()
