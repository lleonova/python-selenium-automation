from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then

ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
NUMBER_OF_ITEMS = (By.ID, "sc-subtotal-label-activecart")
FIRST_PRODUCT_IN_THE_SEARCH = (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")


@then('Click on first product in the search')
def select_product(context):
    one_element = context.driver.wait.until(EC.element_to_be_clickable(FIRST_PRODUCT_IN_THE_SEARCH)).click()


@then('Click Add To Cart Button')
def click_add_to_cart_button(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BUTTON)).click()


@then('Verify that cart has {quantity}')
def how_many_items_in_the_cart(context, quantity):
    items_in_cart = context.driver.wait.until(EC.visibility_of_element_located(NUMBER_OF_ITEMS)).text
    print(items_in_cart)
    assert quantity in items_in_cart, f'Expected {quantity}, but got {items_in_cart}'