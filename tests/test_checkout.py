from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(browser):
    # Login
    login = LoginPage(browser)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Add to cart
    inventory = InventoryPage(browser)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # Checkout
    cart = CartPage(browser)
    items = cart.get_cart_items()
    assert len(items) == 1

    checkout = CheckoutPage(browser)
    checkout.start_checkout()
    checkout.fill_form("John", "Doe", "12345")
    checkout.finish_order()

    # Confirmation
    message = checkout.get_confirmation()
    assert "THANK YOU FOR YOUR ORDER" in message.upper()
