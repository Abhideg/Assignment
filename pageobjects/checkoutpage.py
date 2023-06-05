from selenium.webdriver.common.by import By


class CheckoutPage:
    # CHECKOUT_BUTTON = (By.XPATH, '//*[@id="checkout"]')
    # FIRST_NAME_INPUT = (By.XPATH, '//*[@id="first-name"]')
    # LAST_NAME_INPUT = (By.XPATH, '//*[@id="last-name"]')
    # ZIP_CODE_INPUT = (By.XPATH, '//*[@id="postal-code"]')
    # CONTINUE_BUTTON = (By.XPATH, '//*[@id="continue"]')
    # FINISH_BUTTON = (By.XPATH, '//*[@id="finish"]')
    # THANK_YOU_MESSAGE = (By.XPATH, '//h2[text()="Thank you for your order!"]')

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_button(self):
        return self.driver.find_element(By.ID, "checkout")

    def enter_first_name(self):
        return self.driver.find_element(By.ID, "first-name")

    def enter_last_name(self):
        return self.driver.find_element(By.ID, "last-name")

    def enter_zip_code(self):
        return self.driver.find_element(By.ID, "postal-code")

    def click_continue_button(self):
        return self.driver.find_element(By.ID, "continue")

    def click_finish_button(self):
        return self.driver.find_element(By.ID, "finish")

    def get_thank_you_message(self):
        return self.driver.find_element(By.XPATH, '//h2[text()="Thank you for your order!"]').text
