"""
This module contains EquipmentPage,
"""

from selenium.webdriver.common.by import By


class EquipmentPage:
    # Locators
    EQUIP_EDIT_FIELD = (By.ID, "input-edit-field")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def get_edit_field_name_text(self):
        edit_field_txt = self.browser.find_element(*self.EQUIP_EDIT_FIELD)
        return edit_field_txt.get_property("value")
