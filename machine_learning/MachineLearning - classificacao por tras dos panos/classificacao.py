# -*- coding: utf-8 -*-
#ele é gordinho?   tem perninha curta?   faz auau?
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cao1 = [1, 1, 1]
cao2 = [0, 1, 1]
cao3 = [0, 1, 1]

dados = [porco1, porco2, porco3,
         cao1, cao2, cao3]
# se porco = 1, se cachorro = -1
marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

misterioso1 = [1, 1, 1]   #quem é esse animal misterioso? porco ou cão?
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

teste = [misterioso1, misterioso2, misterioso3]
total_de_testes = len(teste)

marcacoes_teste = [-1, 1, -1]

resultado = modelo.predict(teste)
diferencas = resultado - marcacoes_teste

acertos = [True if int(d)==0 else False for d in diferencas]
print(resultado)
print(acertos)

total_de_acertos = sum(acertos)
taxa_de_acertos = (total_de_acertos/total_de_testes) * 100
print(taxa_de_acertos)