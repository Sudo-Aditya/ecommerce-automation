class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        return self.driver.find_elements("class name", "inventory_item_name")
