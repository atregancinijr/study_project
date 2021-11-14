import json
from keywords.login import LoginPage
from keywords.initial_page import InitialPage
from keywords.equipment_page import EquipmentPage
from keywords.transponder_page import TransponderPage
from keywords.account_page import AccountPage

def json_file():
    with open('test/config.json') as config_file:
        config = json.load(config_file)
    yield config
    config.close()

class Initialization:
    __instance = None

    config = json_file()

    def __init__(self, config=config):
        if not Initialization.__instance:
            self.login_page = LoginPage(config['browser'], config['server'])
            self.initial_page = InitialPage(config['browser'])
            self.equipment_page = EquipmentPage(config['browser'])
            self.transponder_page = FamilyPage(config['browser'], config['server'], config['product_code'], config['serial_number'])
            self.account_page = AccountPage(config['browser'], config['server'])
            print('__init__ method called..')
        else:
            print(f'Instance already created: {self.getInstance()}')

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Initialization()
        return cls.__instance
