from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """Page Object for the TutorialsNinja home page."""

    SEARCH_FIELD = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_product(self, product_name):
        """Search for a product using the homepage search bar."""

        search_field = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_FIELD)
        )

        search_field.clear()
        search_field.send_keys(product_name)

        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        ).click()