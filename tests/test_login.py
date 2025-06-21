from pages.login_page import LoginPage

def test_valid_login(browser):
    page = LoginPage(browser)
    page.load()
    page.login("standard_user", "secret_sauce")
    
    assert "inventory.html" in browser.current_url

def test_invalid_login(browser):
    page = LoginPage(browser)
    page.load()
    page.login("standard_user", "wrong_password")

    # Check if the error message is visible
    error = browser.find_element("css selector", "h3[data-test='error']")
    assert "Username and password do not match" in error.text

