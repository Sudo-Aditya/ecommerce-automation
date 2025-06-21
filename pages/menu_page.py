from selenium.webdriver.common.by import By
import time

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        time.sleep(1)  # wait for menu animation
        self.driver.find_element(*self.logout_link).click()
