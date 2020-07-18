from selenium.webdriver.common.by import By
from pages.base_page import Page

class ShopCart(Page):
    RESULTS_INFO = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty h2")

    def verify_empty_cart_message(self, text, *locator):
        message = self.find_element(*self.RESULTS_INFO).text
        assert text in message, f'Expected to see empty card, but got {message}'
