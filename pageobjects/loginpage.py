from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def set_login(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login-button").click()

    def complete_login(self, username, password):
        self.set_login(username)
        self.set_password(password)
        self.click_login_button()
