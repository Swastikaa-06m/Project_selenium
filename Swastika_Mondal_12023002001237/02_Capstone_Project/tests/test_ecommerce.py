from selenium.webdriver.common.by import By

from utils.driver_factory import create_driver
from utils.screenshot_helper import capture_screenshot
from utils.test_data_reader import load_test_data
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


APPLICATION_URL = "https://tutorialsninja.com/demo/"

def test_load_test_data():
    """Verify that test data can be loaded from JSON."""

    test_data = load_test_data()

    assert test_data["application"]["url"] == "https://tutorialsninja.com/demo/"
    assert test_data["login"]["email"]
    assert test_data["login"]["password"]
    assert test_data["product"]["search_keyword"] == "Nikon"
    assert test_data["product"]["quantity"] == 2


def test_launch_application(driver):
    """Verify that the e-commerce application launches successfully."""
    driver.get(APPLICATION_URL)

    assert "Your Store" in driver.title

    capture_screenshot(driver, "01_application_launch")


def test_login():
    """Verify that a registered user can log in successfully."""

    test_data = load_test_data()

    driver = create_driver()

    try:
        driver.get(test_data["application"]["url"])

        login_page = LoginPage(driver)

        login_page.open_login_page()

        login_page.login(
            test_data["login"]["email"],
            test_data["login"]["password"]
        )

        assert "My Account" in driver.page_source

        capture_screenshot(driver, "02_successful_login")

    finally:
        driver.quit()

def test_product_search():
    """Verify that a product can be searched successfully."""

    test_data = load_test_data()

    driver = create_driver()

    try:
        driver.get(test_data["application"]["url"])

        home_page = HomePage(driver)

        home_page.search_product(
            test_data["product"]["search_keyword"]
        )

        assert "Search" in driver.title

        assert "Nikon" in driver.page_source

        capture_screenshot(driver, "03_product_search")

    finally:
        driver.quit()

def test_add_product_to_cart():
    """Verify that a searched product can be added to the cart."""

    test_data = load_test_data()

    driver = create_driver()

    try:
        driver.get(test_data["application"]["url"])

        home_page = HomePage(driver)
        home_page.search_product(
            test_data["product"]["search_keyword"]
        )

        product_page = ProductPage(driver)

        product_page.add_product_to_cart()

        message = product_page.get_success_message()

        assert "Success" in message
        assert "shopping cart" in message

        capture_screenshot(driver, "04_product_added_to_cart")

    finally:
        driver.quit()

def test_update_cart_quantity_and_verify_details():
    """Verify cart quantity and product pricing details."""

    test_data = load_test_data()

    driver = create_driver()

    try:
        driver.get(test_data["application"]["url"])

        home_page = HomePage(driver)

        home_page.search_product(
            test_data["product"]["search_keyword"]
        )

        product_page = ProductPage(driver)

        product_page.add_product_to_cart()

        cart_page = CartPage(driver)

        cart_page.open_cart()

        cart_page.update_quantity(
            test_data["product"]["quantity"]
        )

        success_message = cart_page.get_success_message()

        assert "Success" in success_message
        assert "shopping cart" in success_message

        assert cart_page.get_product_name() == "Nikon D300"

        assert cart_page.get_quantity() == 2

        assert "$98.00" in cart_page.get_unit_price()

        assert "$196.00" in cart_page.get_total_price()

        capture_screenshot(
            driver, "05_cart_quantity_and_details"
        )

    finally:
        driver.quit()