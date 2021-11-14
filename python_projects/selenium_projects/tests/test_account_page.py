"""
These tests cover Account page.
"""
import pytest
from time import sleep
from keywords.login import LoginPage
from keywords.account_page import AccountPage

def test_enter_account_configuration(browser, config):
    account_page = AccountPage(browser, config['server'])
    # Enter in the account configuration
    account_page.enter_account_page()

    # then confirm that is in Account Configuration page
    language = account_page.get_language()
    assert language == 'Português' or language == 'English' or language == 'Español'


@pytest.mark.parametrize('language_change', ['English', 'Português', 'Español'])
def test_change_account_configuration_language(browser, config, language_change):
    dict_language = {'English': ('Language', 'User', 'Password'), 'Português': ('Idioma', 'Usuário', 'Senha'), 'Español': ('Idioma', 'Usuario', 'Contraseña')}
    account_page = AccountPage(browser, config['server'])
    # Given the server account page is displayed
    account_page.load()

    # When the user change the language
    account_page.change_language(language_change)

    # Then the Language configuration has changed correctly
    language = account_page.get_language()
    assert language == language_change
    # When the configuration is saved
    account_page.save_configuration()
    language, user, password = account_page.get_page_keys_labels()
    # Then the page changes the language
    assert (language, user, password) == dict_language[language_change]





