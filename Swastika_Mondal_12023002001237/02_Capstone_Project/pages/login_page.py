from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object for the TutorialsNinja login page."""

    MY_ACCOUNT = (By.XPATH, "//span[contains(text(),'My Account')]")
    LOGIN_LINK = (By.LINK_TEXT, "Login")

    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self):
        """Open the Login page from the My Account menu."""

        self.wait.until(
            EC.element_to_be_clickable(self.MY_ACCOUNT)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_LINK)
        ).click()

    def login(self, email, password):
        """Enter credentials and submit the login form."""

        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )

        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        )

        email_field.clear()
        email_field.send_keys(email)

        password_field.clear()
        password_field.send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()