from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    """Page Object for product search results and product actions."""

    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//button[contains(@onclick, 'cart.add')]"
    )

    SUCCESS_ALERT = (
        By.CSS_SELECTOR,
        ".alert-success"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self):
        """Add the selected product to the shopping cart."""

        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )

        add_to_cart_button.click()

    def get_success_message(self):
        """Return the success alert text after adding the product."""

        success_alert = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT)
        )

        return success_alert.text