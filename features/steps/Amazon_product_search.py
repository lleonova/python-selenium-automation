from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys




# RESULTS_INFO_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
#RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Amazon page')
def open_amazon(context):
   # context.driver.get('https://www.amazon.com/')
    context.app.page.open_page()


@when('Search for {search_word}')
def input_search(context, search_word):
    # search = context.driver.find_element(*SEARCH_INPUT)
    # search.clear()
    # search.send_keys(search_word)
    # sleep(4)
    context.app.top_nav_menu.search_word(search_word)

#
# @when('Click on search icon')
# def click_search_icon(context):
#     context.driver.find_element(*SEARCH_SUBMIT).click()
#     sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    # results_msg = context.driver.find_element(*RESULTS_INFO_TEXT).text
    # assert search_word in results_msg, f'Expected word {search_word} in message, but got {results_msg}'
    context.app.search_results_page.verify_found_results_text(search_word)


# @then('First result contains {search_word}')
# def verify_first_result(context, search_word):
#     first_result = context.driver.find_element(*RESULTS).text
#     print('\n{}'.format(first_result))
#     assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)

@when('Select {alias} department')
def select_department(context, alias):
    context.app.top_nav_menu.select_department(alias)

@then('{selected_dep} department is selected')
def verify_selected_department(context, selected_dep):
    context.app.top_nav_menu.verify_selected_department(selected_dep)