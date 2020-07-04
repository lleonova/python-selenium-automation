from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then

DEALS_SELECTION = (By.CSS_SELECTOR, ".wfm-sales-item-card__regular-price")
PRODUCT_NAMES = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")

@given('Open Amazon WholeFoods Deals page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals ')


@then("Verify that every product on the page has a text {keyword}")
def product_has_word_regular(context, keyword):
    for item in context.driver.wait.until(EC.presence_of_all_elements_located(DEALS_SELECTION)):
#    for item in context.driver.find_elements(*DEALS_SELECTION):
#        print(item.text, keyword)
        assert keyword in item.text


@then("Verify that every product on the page has a product name")
def product_has_name(context):
 #   for item in context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_NAMES)):
    for item in context.driver.find_elements(*PRODUCT_NAMES):
        assert item.text != ''
 #       print(item.text)

