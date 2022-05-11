def my_model(model_obj, train_x, train_y, test_x, test_y):
    modelo = model_obj
    modelo.fit(train_x, train_y)

    resultado = modelo.predict(test_x)

    acertos = resultado == test_y

    total_de_acertos = sum(acertos)
    total_de_elementos = len(test_x)
    #print(f'total de elementos: {total_de_elementos}')
    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

    print(f'taxa de acertos do modelo teste {str(model_obj)}: {taxa_de_acerto}%')
    return modelo, taxa_de_acerto

def taxa_de_acerto_base(y):
    acerto_de_um = len(y[y==True])
    acerto_de_zero =  len(y[y==False])
    taxa_de_acerto_base = 100.0 * max(acerto_de_um, acerto_de_zero)/len(y)
    print(f'Taxa de acerto base: {taxa_de_acerto_base}%')