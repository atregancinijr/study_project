from dados import carregar_dados
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X,Y = carregar_dados('acesso.csv')

seed = 5

treino_x, teste_x, treino_y, teste_y = train_test_split(X, Y, random_state = seed, test_size = 0.25) 
modelo = MultinomialNB()
modelo.fit(treino_x, treino_y)

previsoes = modelo.predict(teste_x)

taxa_de_acertos = accuracy_score(teste_y, previsoes)

print(f"Taxa de acertos: {round(taxa_de_acertos*100)} %")
