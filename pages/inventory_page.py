class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = "shopping_cart_link"

    def add_first_item_to_cart(self):
        self.driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()

    def go_to_cart(self):
        self.driver.find_element("class name", self.cart_link).click()
