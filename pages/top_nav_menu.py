from selenium.webdriver.common.by import By
from pages.base_page import Page

class TopNavMenu(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.XPATH, "//input[@value='Go']")
    RETURNS_AND_ORDERS_BUTTON = (By.ID, 'nav-orders')
    ITEMS_IN_THE_CART = (By.ID, "nav-cart-count")
    CART_ICON = (By.ID, 'nav-cart')
    HAM_MENU = (By.ID, "nav-hamburger-menu")


    def search_word(self, search_word):
        self.input(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)

    def click_on_returns_and_orders(self, *locator):
        self.click(*self.RETURNS_AND_ORDERS_BUTTON)

    def shopping_cart_counter(self, amount: int, *locator):
        self.verify_text(amount, *self.ITEMS_IN_THE_CART)

    def click_shopping_cart(self, *locator):
        self.click(*self.CART_ICON)

    def click_h_m(self, *locator):
        self.wait_for_element_click(*self.HAM_MENU)


