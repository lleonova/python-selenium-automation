from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR =(By.CSS_SELECTOR, "div#variation_color_name span.selection")
EXPECTED_COLORS = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse', 'Vintage Light Wash']
#IMAGE_OPTIONS = (By.CSS_SELECTOR, "img.imgSwatch")



@given('Open Amazon {product_id} product page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then('Verify user can select through color choices')
def verify_color_selection(context):

    color_options = context.driver.wait.until(EC.presence_of_all_elements_located(COLOR_OPTIONS))
    for ind in range(len(color_options)):
        color_options[ind].click()
        selected_color_text = context.driver.find_element(*SELECTED_COLOR).text
        assert selected_color_text == EXPECTED_COLORS[ind]
