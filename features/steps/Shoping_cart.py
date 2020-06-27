from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then


ITEMS_IN_THE_CART = (By.ID, "nav-cart-count")
CART_ICON = (By.ID, 'nav-cart')
RESULTS_INFO = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty h2")

@when('Amazon Shopping Cart has {number} items')
def verify_shopping_cart_is_empty(context, number):
    result_qty = context.driver.wait.until(EC.visibility_of_element_located(ITEMS_IN_THE_CART)).text
    assert number in result_qty, f'Expected quantity 0 in message, but got {result_qty}'


@when('Click on Shopping Cart icon')
def click_shopping_cart_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(CART_ICON)).click()


@then('Verify that {key_phrase}')
def verify_found_results_text(context, key_phrase):
    results_msg = context.driver.wait.until(EC.visibility_of_element_located(RESULTS_INFO)).text
    assert key_phrase in results_msg, f'Expected {key_phrase}, but got {results_msg}'


