"""
This module contains InitialPage,
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class InitialPage:
    # Locators
    SEARCH_INPUT = (By.XPATH, '//*[@class="p-autocomplete-input p-inputtext p-component p-autocomplete-dd-input"]')
    SEARCH_SPAN_LIST = (By.XPATH, '//*[@class="p-autocomplete-items p-autocomplete-list p-component"]/li')
    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def find_titles_in_dashboards(self, title):
        #DASHBOARDS_TEXT = (By.CSS_SELECTOR, f'dashboard-card {title}')
        #dashboard_text = self.browser.find_element(*DASHBOARDS_TEXT)
        #return dashboard_text.text()
        #TO DO
        pass

    def search_network_elements(self, element):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(element)

    def click_element_listed_by_search(self, element):
        self.SEARCH_SPAN_LIST[1].join(f'/div/span[text()="{element}"]')
        list_found = self.browser.find_element(*self.SEARCH_SPAN_LIST)
        list_found.click()

    def title(self):
        WebDriverWait(self.browser, 10).until(ec.title_contains(""))
        return self.browser.title
