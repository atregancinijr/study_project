class Pessoa:
    def __init__(self, nome, idade):    #AQUI TEMOS O CONSTRUTOR
        self.nome = nome                #AQUI TEMOS OS ATRIBUTOS DA CLASSE
        self.idade = idade

    def get_pessoa(self):               #AQUI TEMOS UMA FUNÇÃO DA CLASSE
        return f'({self.nome, self.idade})'

    def __repr__(self):
        return f'{self.nome}, {self.idade}'

if __name__ == '__main__':
    p = Pessoa('Anderson', 30)          #"p" É UM OBJETO DO TIPO Pessoa
    print(f'Descreva o Objeto: {p} \nEndereço de memória: {id(p)}')
    print(p)
