from selenium.webdriver.common.by import By
from behave import then
from time import sleep

LINKS = (By.CSS_SELECTOR, "#zg_tabs a")
BANNERS = (By.CSS_SELECTOR, "#zg_banner_text_wrapper")


@then("Verify that each Top Menu link opens up a corresponding page")
def open_links(context):

    bestseller_page_links = context.driver.find_elements(*LINKS)

    for index in range(len(bestseller_page_links)):

        link = context.driver.find_elements(*LINKS)[index]
        expected_text = link.text
        link.click()
        sleep(1)
        actual_text = context.driver.find_element(*BANNERS).text
        assert expected_text in actual_text, f'Expected to see {link.text} in the banner, but got {actual_text}'