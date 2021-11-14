"""
This module contains AccountPage
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
class AccountPage:
    # Locators
    PROFILE_BUTTON = (By.XPATH, f'//button[@class="p-link layout-profile-link"]/div/span[@class="user-span"]')
    USER_OPTION = (By.XPATH, '//*[@id="overlay_menu"]/ul/li[1]/a')
    IDIOM_LABEL = (By.XPATH, '//label[@class ="p-dropdown-label p-inputtext"]')
    IDIOM_LIST = (By.XPATH, '//ul[@class="p-dropdown-items p-dropdown-list p-component"]')
    IDIOM_BUTTON = (By.XPATH, '//div[@role="button" and @class="p-dropdown-trigger"]/span')
    SAVE_BUTTON = (By.ID, "button-save")
    PAGE_KEY_LABELS_BASE = '//div[@class="layout-main"]'
    LANGUAGE_LABEL = (By.XPATH, PAGE_KEY_LABELS_BASE + '/div/section[1]/span')
    USER_LABEL = (By.XPATH, PAGE_KEY_LABELS_BASE + '/div/section[2]/span')
    PASSWORD_LABEL = (By.XPATH, PAGE_KEY_LABELS_BASE + '/div/section[3]/span')

    # Initializer
    def __init__(self, browser, server):
        self.browser = browser
        self.URL = f'http://{server}/account'

    def load(self):
        self.browser.get(self.URL)

    def enter_account_page(self):
        profile_bt = self.browser.find_element(*self.PROFILE_BUTTON)
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(self.PROFILE_BUTTON))
        profile_bt.click()
        user_opt = self.browser.find_element(*self.USER_OPTION)
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(self.USER_OPTION))
        user_opt.click()

    # Interaction Methods
    def change_language(self, language):
        IDIOM_LIST_ELEMENT = (By.XPATH, f'//li[@aria-label="{language}"]')
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(self.IDIOM_BUTTON))
        idiom_button = self.browser.find_element(*self.IDIOM_BUTTON)
        idiom_button.click()
        sleep(0.5)
        idiom_list = self.browser.find_element(*self.IDIOM_LIST)
        idiom_list_element = self.browser.find_element(*IDIOM_LIST_ELEMENT)
        WebDriverWait(self.browser, 10).until(ec.visibility_of(idiom_list))
        idiom_list_element.click()

    def get_language(self):
        idiom_label = self.browser.find_element(*self.IDIOM_LABEL)
        WebDriverWait(self.browser, 10).until(ec.visibility_of(idiom_label))
        configured_language = idiom_label.get_attribute("innerText")
        print(f'Configured Language: {configured_language}')
        return configured_language

    def save_configuration(self):
        WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable(self.SAVE_BUTTON))
        save_button = self.browser.find_element(*self.SAVE_BUTTON)
        save_button.click()

    def get_page_keys_labels(self):
        WebDriverWait(self.browser.find_element(*self.LANGUAGE_LABEL), 5)
        lang_label = self.browser.find_element(*self.LANGUAGE_LABEL)
        user_label = self.browser.find_element(*self.USER_LABEL)
        pwrd_label = self.browser.find_element(*self.PASSWORD_LABEL)
        lang_label_text = lang_label.get_attribute("innerText")
        user_label_text = user_label.get_attribute("innerText")
        pwrd_label_text = pwrd_label.get_attribute("innerText")
        return lang_label_text, user_label_text, pwrd_label_text
