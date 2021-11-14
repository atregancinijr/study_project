class Pessoa:
    def __init__(self, nome, altura):
        self.__nome = nome
        self.__altura = altura

    def __lt__(self, other):  #"<"
        if self.__altura < other.__altura:
            return f'{self.__nome} é mais baixo que {other.__nome}'
        else:
            return f'{self.__nome} NÃO é mais baixo que {other.__nome}'

    def __le__(self, other):  #"<="
        if self.__altura <= other.__altura:
            return f'{self.__nome} é mais baixo ou tem a mesma altura que {other.__nome}'
        else:
            return f'{self.__nome} NÃO é mais baixo ou tem a mesma altura que {other.__nome}'

    def __gt__(self, other):  #">"
        if self.__altura > other.__altura:
            return f'{self.__nome} é mais alto que {other.__nome}'
        else:
            return f'{self.__nome} NÃO é mais alto que {other.__nome}'

    def __ge__(self, other):  #">="
        if self.__altura >= other.__altura:
            return f'{self.__nome} é mais alto ou tem a mesma altura que {other.__nome}'
        else:
            return f'{self.__nome} NÃO é mais alto ou tem a mesma altura que {other.__nome}'

if __name__ == '__main__':
    pessoa1 = Pessoa('Joao', 173)
    pessoa2 = Pessoa('Maria', 161)
    pessoa3 = Pessoa('Pedro', 159)
    pessoa4 = Pessoa('Ana', 173)
    pessoa5 = Pessoa('Gustavo', 161)

    print(pessoa1 < pessoa2)
    print(pessoa3 < pessoa2)
    print(pessoa5 <= pessoa2)
    print(pessoa1 > pessoa4)
    print(pessoa1 >= pessoa4)

