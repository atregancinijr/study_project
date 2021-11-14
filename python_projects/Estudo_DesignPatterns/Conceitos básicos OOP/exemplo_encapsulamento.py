class ADM_rights():
    def __init__(self, senha):
        self.__senha = senha

    def valida_permissao_de_adm(self):
        if self.__senha == 'Admin123':
            permition = True
        else:
            permition = False
        return permition

class Pessoa(ADM_rights):
    def __init__(self, nome, idade, senha=''):
        self.__nome = nome
        self.idade = idade
        super().__init__(senha)
        self.__permition = self.valida_permissao_de_adm()

    def qual_seu_nome(self):
        print(f'Meu nome é {self.__nome}')

    def __eh_um_administrador(self):
        return 'É um administrador.' if self.__permition==True else 'Não é um administrador.'

    def muda_nome_da_pessoa(self, novo_nome):
        if self.__permition==True:
            print(f'Mudança do nome {self.__nome} para {novo_nome}.')
            self.__nome = novo_nome
        else:
            print(f'Não é possível mudar o seu nome. {self.__eh_um_administrador()}')


if __name__== '__main__':
    pessoa1 = Pessoa('Edvanilsanderson', 17, 'Admin123')

    print(pessoa1.idade)  #Perceba que eu consigo ler o atributo idade, mas não consigo ler o atributo nome, dado que
                          #este é protegido (observe o '__' a esqueda de 'nome')
    pessoa1.idade = 18
    print(pessoa1.idade)

    try:
        print(pessoa1.__nome)
    except:
        try:
            print(pessoa1.nome)
        except:
            print('Não é possivel acessar o atributo nome diretamente. Tente usar o método \'qual_seu_nome\'')

    pessoa1.qual_seu_nome()

    #Supondo que Edvanilsanderson não gosta do seu próprio nome e quer mudar para João.
    #Como ele faria, dado que o atributo nome da classe Pessoa é protegido (privado)?
    #Para tal, utilizaremos uma outra função para fazer isto, por exemplo.

    pessoa1.muda_nome_da_pessoa('João')
    pessoa1.qual_seu_nome()