from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.ID, 'helpsearch')
SEARCH_SUBMIT = (By.XPATH, "//input[@class='a-button-input']")
RESULTS_INFO_TEXT = (By.XPATH, "//h1[text() = 'Cancel Items or Orders']")

@given('Open Amazon Help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_word} into Help search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on Help search icon')
def click_search_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT)).click()

@then('Product results for Help {search_word} are shown')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.wait.until(EC.visibility_of_element_located(RESULTS_INFO_TEXT)).text
    assert search_word in results_msg, f'Expected word {search_word} in message, but got {results_msg}'



# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#     results_msg = context.driver.find_element(*RESULTS_INFO_TEXT).text
#     assert search_word in results_msg, f'Expected word {search_word} in message, but got {results_msg}'
