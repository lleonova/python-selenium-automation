from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page



class Product(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    SIZE_SELECTION_TOOLTIP = (By.ID, 'a-popover-content-1')
    NEW_ARRIVALS_MENU = (By.CSS_SELECTOR, "div#nav-subnav a:nth-child(7)")
    DEALS = (By.ID, 'nav-flyout-aj:https://images-na.ssl-images-amazon.com/images/G/01/softlines/megamenu/prod/megamenu-contents_en_US._TTH_.json:subnav-sl-megamenu-8:0')

    def open_product(self, product_id):
        self.open_product(f'dp/{product_id}')

    def hover_add_to_cart(self):
        cart_button = self.find_element(*self.ADD_TO_CART_BTN)
        self.actions.move_to_element(cart_button)
        self.actions.perform()
        sleep(2)

    def verify_size_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_SELECTION_TOOLTIP)

    def hover_over_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS_MENU)
        self.actions.move_to_element(new_arrivals)
        self.actions.perform()
        sleep(2)

    def verify_new_arrivals(self):
        self.wait_for_element_appear(*self.DEALS)


