from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then

BESTSELLERS_ICON = (By.CSS_SELECTOR, "a[href*='bestsellers']")
BESTSELLERS_LINKS =(By.CSS_SELECTOR, "#zg_tabs li")

@then('Click on BestSellers icon')
def click_shopping_cart_icon(context):
    #context.driver.wait.until(EC.element_to_be_clickable(BESTSELLERS_ICON)).click()
    context.driver.find_element(*BESTSELLERS_ICON).click()


@then('Verify that page has {number} links displayed')
def verify_ammount_of_links(context, number):
    expected_ammount_of_links = int(number)
    actual_ammount_of_links = len(context.driver.find_elements(*BESTSELLERS_LINKS))
    print(actual_ammount_of_links)
    assert expected_ammount_of_links ==  actual_ammount_of_links, f'Expected {number} links, but got {actual_ammount_of_links}'