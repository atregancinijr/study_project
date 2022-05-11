# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from utils import my_model, taxa_de_acerto_base
import random

#teste inicial: home, busca, logado => comprou

df = pd.read_csv('busca.csv')    #df == dataframe, formato 'bonito', estruturado

print(df.head())

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

print(X_df.head())
print(pd.get_dummies(X_df).head())

Xdummies_df = pd.get_dummies(X_df).astype(int)  # com estes dados, a coluna 'busca' que era string (algoritmos, java, ruby)...
#foi corretamente transformada em três colunas com valores binários
Ydummies_df = Y_df

X = Xdummies_df.values        #pelo apenas os valores aqui, deixo de ser df
Y = Ydummies_df.values

index_list = [d for d in range(0, len(Y))]
random.shuffle(index_list)

X = X[index_list]
Y = Y[index_list]
# dict2 = {'home': X[:, 0], 'logado': X[:, 1], 'busca_algoritmos':X[:, 2], 'busca_java':X[:, 3], 'busca_ruby':X[:, 4], 'comprou': Y}
# df = pd.DataFrame(dict2)
# df.to_csv('file2.csv', index=False)

porcentagem_treino = 0.8
porcentagem_de_teste = 0.1

tamanho_de_treino = int(porcentagem_treino * len(Y))
tamanho_de_teste = round(porcentagem_de_teste * len(Y))
tamanho_de_validacao = len(Y) - tamanho_de_treino - tamanho_de_teste

train_x = X[:tamanho_de_treino]
train_y = Y[:tamanho_de_treino]

test_x = X[tamanho_de_treino:(tamanho_de_teste+tamanho_de_treino)]
test_y = Y[tamanho_de_treino:(tamanho_de_teste+tamanho_de_treino)]

validation_x = X[(tamanho_de_teste+tamanho_de_treino):(tamanho_de_teste+tamanho_de_treino+tamanho_de_validacao)]
validation_y = Y[(tamanho_de_teste+tamanho_de_treino):(tamanho_de_teste+tamanho_de_treino+tamanho_de_validacao)]
print(f'train_x:\n{pd.DataFrame(train_x)}')
print(f'train_y:\n{pd.DataFrame(train_y)}')
print(f'test_x:\n{pd.DataFrame(test_x)}')
print(f'test_y:\n{pd.DataFrame(test_y)}')
print(f'validation_x:\n{pd.DataFrame(validation_x)}')
print(f'validation_y:\n{pd.DataFrame(validation_y)}')


taxa_de_acerto_base(test_y)

res1 = my_model(MultinomialNB(), train_x, train_y, test_x, test_y)
res2 = my_model(AdaBoostClassifier(), train_x, train_y, test_x, test_y)

results = [res1, res2]

max_porcentagem_de_acertos = 0.0
for idx, res in enumerate(results):
    if max_porcentagem_de_acertos <= res[1]:
        modelo = res[0]
        max_porcentagem_de_acertos = res[1]
print(f'modelo vencedor: {str(modelo)}')
resultado = modelo.predict(validation_x)
acertos = resultado == validation_y
total_de_acertos = sum(acertos)
total_de_elementos = len(validation_x)
#print(f'total de elementos: {total_de_elementos}')
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(f'taxa de acertos do modelo validacao {str(modelo)}: {taxa_de_acerto}%')