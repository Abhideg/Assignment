from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    CART_ICON = (By.XPATH, '//*[@id="shopping_cart_container"]')
    PRODUCT_NAME = (By.XPATH, '//*[text()="Sauce Labs Backpack"]')
    cart_item = (By.XPATH, '//*[text()="Sauce Labs Backpack"]')

    def click_add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def click_cart_icon(self):
        self.driver.find_element(*self.CART_ICON).click()

    def get_product_name(self):
        return self.driver.find_element(*self.PRODUCT_NAME).text

    def get_cart_items(self):
        return self.driver.find_element(*self.cart_item).text
