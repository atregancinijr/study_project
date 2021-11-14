from project.buraco import Buraco
from project.cilindro import Cilindro
from project.paralelepipedo_regular import ParalelepipedoRegular
from project.adaptador import ParapelepipedoAdapter


def verifica_se_o_cilindro_entra_no_buraco(buraco, cilindro):
    print(f'Sucesso! O {cilindro.id} coube no buraco.') if buraco.fits(cilindro) else print('Falha! A peça não coube no buraco.')


if __name__ == '__main__':
    buraco = Buraco(20, 30)
    print(buraco)
    cilindro = Cilindro(10, 10)
    print(cilindro)

    verifica_se_o_cilindro_entra_no_buraco(buraco, cilindro)

    paralelepipedo_regular = ParalelepipedoRegular(5, 20)
    print(paralelepipedo_regular)

    try:
        verifica_se_o_cilindro_entra_no_buraco(buraco, paralelepipedo_regular)
    except AttributeError:
        print('Eita! Isso não me parece um cilindro não! Não sei brincar com isso não meu jovem.')

    paralelepipedo_adaptado = ParapelepipedoAdapter(paralelepipedo_regular.lado, paralelepipedo_regular.altura)
    print(paralelepipedo_adaptado)

    verifica_se_o_cilindro_entra_no_buraco(buraco, paralelepipedo_adaptado)
