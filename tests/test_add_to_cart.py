from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_item_to_cart(browser):
    # Login
    login = LoginPage(browser)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Add item and go to cart
    inventory = InventoryPage(browser)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # Verify item in cart
    cart = CartPage(browser)
    items = cart.get_cart_items()
    assert len(items) == 1
    assert items[0].text == "Sauce Labs Backpack"
