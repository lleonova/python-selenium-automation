from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResults(Page):
    RESULTS_INFO_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_found_results_text(self, search_word):
        search_result_header = self.find_element(*self.RESULTS_INFO_TEXT).text
        assert search_word in search_result_header, f'Expected word {search_word} in message, but got {search_result_header}'