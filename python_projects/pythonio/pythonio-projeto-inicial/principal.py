from contato_utils import csv_para_contatos, contatos_para_pickle, pickle_para_contatos
from contato_utils import contatos_para_json, json_para_contato
try:
    #contatos = csv_para_contatos('dados/contatos.csv')
    #contatos_para_pickle(contatos, 'dados/contatos.pickle')

    #contatos = pickle_para_contatos('dados/contatos.pickle')
    #contatos_para_json(contatos, 'dados/contatos.json')
    contatos = json_para_contato('dados/contatos.json')
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')