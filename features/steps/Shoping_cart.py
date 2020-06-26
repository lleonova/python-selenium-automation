from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

ITEMS_IN_THE_CART = (By.ID, "nav-cart-count")
CART_ICON = (By.ID, 'nav-cart')
RESULTS_INFO = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty h2")

SEARCH_SUBMIT = (By.XPATH, "//input[@value='Go']")
RESULTS_INFO = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty")


@when('Amazon Shoppin Cart has 0 items')
def verify_shopping_cart_is_empty(context):
    result_qty = context.driver.wait.until(EC.visibility_of_element_located(ITEMS_IN_THE_CART)).text
    assert '0' in result_qty, f'Expected quantity 0 in message, but got {result_qty}'


@when('Click on Shopping Cart icon')
def click_shopping_cart_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(CART_ICON)).click()


@then('Verify that Amazon Cart is empty')
def verify_found_results_text(context):
    results_msg = context.driver.wait.until(EC.visibility_of_element_located(RESULTS_INFO)).text
    assert 'empty' in results_msg, f'Expected empty cart, but got {results_msg}'


