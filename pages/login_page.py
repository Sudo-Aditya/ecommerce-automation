class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = "user-name"
        self.password_input = "password"
        self.login_button = "login-button"

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element("id", self.username_input).send_keys(username)
        self.driver.find_element("id", self.password_input).send_keys(password)
        self.driver.find_element("id", self.login_button).click()
