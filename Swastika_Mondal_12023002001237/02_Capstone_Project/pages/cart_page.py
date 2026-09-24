from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object for the shopping cart page."""

    CART_LINK = (
        By.XPATH,
        "//a[contains(@href, 'checkout/cart')]"
    )

    QUANTITY_FIELD = (
        By.CSS_SELECTOR,
        "input[name^='quantity']"
    )

    UPDATE_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-original-title='Update']"
    )

    SUCCESS_ALERT = (
        By.CSS_SELECTOR,
        ".alert-success"
    )

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "div.table-responsive table tbody tr td:nth-child(2) a"
    )

    UNIT_PRICE = (
        By.CSS_SELECTOR,
        "div.table-responsive table tbody tr td:nth-child(5)"
    )

    TOTAL_PRICE = (
        By.CSS_SELECTOR,
        "div.table-responsive table tbody tr td:nth-child(6)"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):
        """Open the shopping cart."""

        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()

    def update_quantity(self, quantity):
        """Update the quantity of the cart item."""

        quantity_field = self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_FIELD)
        )

        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

        self.wait.until(
            EC.element_to_be_clickable(self.UPDATE_BUTTON)
        ).click()

    def get_success_message(self):
        """Return the cart update success message."""

        success_alert = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT)
        )

        return success_alert.text

    def get_product_name(self):
        """Return the product name displayed in the cart."""

        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text

    def get_quantity(self):
        """Return the current cart quantity."""

        quantity_field = self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_FIELD)
        )

        return int(quantity_field.get_attribute("value"))

    def get_unit_price(self):
        """Return the product unit price."""

        return self.wait.until(
            EC.visibility_of_element_located(self.UNIT_PRICE)
        ).text

    def get_total_price(self):
        """Return the product total price."""

        return self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_PRICE)
        ).text