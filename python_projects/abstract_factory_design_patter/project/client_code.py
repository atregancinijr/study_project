from project.mobilias_concretas import MobiliaVitoriana, MobiliaModerna


def client_code(mobilia):
    print(mobilia)
    cadeira = mobilia.cadeira
    cadeira.sentar()
    sofa = mobilia.sofa
    sofa.sentar()
    sofa.deitar()
    cama = mobilia.cama
    cama.deitar()


if __name__ == '__main__':
    estilo = MobiliaVitoriana()
    client_code(estilo)
    print('\n')
    estilo = MobiliaModerna()
    client_code(estilo)
