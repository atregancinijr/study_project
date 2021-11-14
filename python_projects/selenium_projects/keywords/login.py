"""
This module contains LoginPage
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

class LoginPage:
    # Locators
    LOGIN_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')

    # Initializer
    def __init__(self, browser, server):
        self.browser = browser
        self.server = server
        self.URL = f'http://{self.server}'

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def login(self):
        login_input = self.browser.find_element(*self.LOGIN_INPUT)
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        WebDriverWait(self.browser, 10).until(ec.visibility_of(login_input))
        login_input.send_keys('admin')
        WebDriverWait(self.browser, 10).until(ec.visibility_of(password_input))
        password_input.send_keys('pass')
        password_input.send_keys(Keys.RETURN)
        sleep(0.5)
