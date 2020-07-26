from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select

class TopNavMenu(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.XPATH, "//input[@value='Go']")
    RETURNS_AND_ORDERS_BUTTON = (By.ID, 'nav-orders')
    ITEMS_IN_THE_CART = (By.ID, "nav-cart-count")
    CART_ICON = (By.ID, 'nav-cart')
    HAM_MENU = (By.ID, "nav-hamburger-menu")
    SELECT_DEPARTMENT = (By.ID, 'searchDropdownBox')
    DISPLAYED_DEPARTMENT = (By.CSS_SELECTOR, 'div#nav-subnav .nav-b')


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

    def select_department(self, alias):
        dep_selection_element = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(dep_selection_element)
        select.select_by_value(f'search-alias={alias}')

    def verify_selected_department(self, selected_dep):
        self.verify_text(selected_dep, *self.DISPLAYED_DEPARTMENT)