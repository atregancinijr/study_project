"""
Module containing shared fixtures.

"""

import json
import pytest
import selenium.webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from keywords.login import LoginPage
@pytest.fixture
def config():
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()

    elif config['browser'] == 'Chrome':
        options = selenium.webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        b = selenium.webdriver.Chrome(options=options)

    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        opts.add_experimental_option("excludeSwitches", ["enable-logging"])
        b = selenium.webdriver.Chrome(options=opts)

    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    server_login(b, config['server'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()

def server_login(b, server):
    server_page = LoginPage(b, server)
    # Given login page is displayed
    server_page.load()
    # When the user input the correct login and correct password
    server_page.login()


