from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

RETURNS_AND_ORDERS_BUTTON = (By.ID, 'nav-orders')
EMAIL_FIELD = (By.ID, 'ap_email')
RESULTS_INFO_TEXT = (By.XPATH, "//h1[text() = 'Cancel Items or Orders']")


@when('Click Returns And Orders')
def click_sign_in_button(context):
    context.driver.wait.until(EC.element_to_be_clickable(RETURNS_AND_ORDERS_BUTTON)).click()


@then('Verify Sign In page is opened')
def verufy_signin_opend(context):
    context.driver.wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).click()
    current_url = context.driver.current_url
    assert 'https://www.amazon.com/ap/signin' in current_url, \
    f'Expected url is: "https://www.amazon.com/ap/signin...", Actual url is {current_url}'