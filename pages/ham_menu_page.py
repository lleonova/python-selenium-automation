from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class HamburgerMenu(Page):
    AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, ".hmenu-item[href*='music']")

    def click_amazon_music(self, *locator):
        self.wait_for_element_click(*self.AMAZON_MUSIC_MENU_ITEM)

    def verify_menu_items(self, number):
        self.wait_for_presence_off_all_elements(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS)
    #    self.driver.wait.until(correct_menu_items_present(self.AMAZON_MUSIC_MENU_ITEM_RESULTS, number),"Amount of items is incorrect")
        links = len(self.find_elements(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS))
        assert int(number) == links, f'Expected {number} links, but got {links}'

#
# class correct_menu_items_present(object):
#     def __init__(self, locator, amount):
#         self.locator = locator
#         self.amount = amount
#
#     def __call__(self, driver):
#         elements = driver.find_elements(*self.locator)  # Finding the referenced element
#         if len(elements) == self.amount:
#             return elements
#         else:
#             return False