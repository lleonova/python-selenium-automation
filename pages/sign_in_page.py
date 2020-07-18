from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignIn(Page):
    EMAIL_FIELD = (By.ID, 'ap_email')
    RESULTS_INFO_TEXT = (By.XPATH, "//h1[text() = 'Cancel Items or Orders']")

    def verify_email_field(self):
        email_field = self.find_element(*self.EMAIL_FIELD)
        assert email_field, f'Expected to have email field on the page'
