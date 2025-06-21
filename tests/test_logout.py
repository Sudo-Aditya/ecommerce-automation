from pages.login_page import LoginPage
from pages.menu_page import MenuPage

def test_logout_functionality(browser):
    # Login first
    login = LoginPage(browser)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Logout
    menu = MenuPage(browser)
    menu.logout()

    # Confirm logout worked
    assert "https://www.saucedemo.com/" in browser.current_url
