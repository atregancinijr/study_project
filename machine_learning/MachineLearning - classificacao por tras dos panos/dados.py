# -*- coding: utf-8 -*-
import csv

def carregar_dados(file_name):

    X = []    #informações que eu sei
    Y = []    #informações que eu quero prever

    arquivo = open(file_name, 'r')
    leitor = csv.reader(arquivo)
    leitor.__next__() #joga fora a primeira linha que contem o nome das colunas
    
    for acessou_home, acessou_como_funciona, acessou_contato, comprou in leitor:

        X.append([int(acessou_home), int(acessou_como_funciona), int(acessou_contato)])
        Y.append(int(comprou))

    return X, Y

#Problema: Código repetido, devido aos tipos de dados.
def carregar_buscas(file_name):

    X = []    
    Y = []   

    arquivo = open(file_name, 'r')
    leitor = csv.reader(arquivo)
    next(leitor)    #joga fora a primeira linha que contem o nome das colunas
    
    for home, busca, logado, comprou in leitor:

        X.append([int(home), busca, int(logado)])
        Y.append(int(comprou))

    return X, Y