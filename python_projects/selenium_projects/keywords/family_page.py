"""
This module contains FamilyPage,
"""

from selenium.webdriver.common.by import By
from keywords.equipment_page import EquipmentPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class FamilyPage(EquipmentPage):
    # Locators
    MODEL_PANEL_BASE_XPATH = '//div[@class="panel1"]'
    MODEL_PANEL = (By.XPATH, MODEL_PANEL_BASE_XPATH)
    MODEL_PANEL_UNIT = (By.XPATH, '//div[@class="panel1"]/div/div[2]/div[3]')
    MODEL_PANEL_MODEL = (By.XPATH, MODEL_PANEL_BASE_XPATH + '/div/div[3]/div[3]')
    MODEL_PANEL_FAMILY = (By.XPATH, MODEL_PANEL_BASE_XPATH + '/div/div[@class="container-line"][5]/div[@class="container-value"]')

    # Initializer
    def __init__(self, browser, server, pn, sn):
        super().__init__(browser)
        self.browser = browser
        self.URL = f'http://{server}/ne/board/{pn}/{sn}#details'

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def get_unit(self):
        unit = self.browser.find_element(*self.MODEL_PANEL_UNIT)
        return unit.get_attribute("innerText")

    def get_model(self):
        model = self.browser.find_element(*self.MODEL_PANEL_MODEL)
        return model.get_attribute("innerText")

    def get_family(self):
        family = self.browser.find_element(*self.MODEL_PANEL_FAMILY)
        return family.get_attribute("innerText")
