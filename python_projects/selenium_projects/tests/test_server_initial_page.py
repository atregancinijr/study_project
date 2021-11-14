"""
These tests cover login on Server.
"""
from time import sleep
from keywords.initial_page import InitialPage
from keywords.login import LoginPage
from keywords.equipment_page import EquipmentPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_login(browser):
    initial_page = InitialPage(browser)
    # The initial page has the expected title
    title = initial_page.title()

    assert title == "Title_stub"


def test_search_network_element(browser, config):
    initial_page = InitialPage(browser)
    equipment_page = EquipmentPage(browser)

    board = config['board'] + '#' + config['serial_number']
    # Given the user loggged in server
    # And Search for and network element
    initial_page.search_network_elements(board)
    initial_page.click_element_listed_by_search(board)

    # So the desired element page should be displayed

    equip_name = equipment_page.get_edit_field_name_text()
    assert equip_name == board


