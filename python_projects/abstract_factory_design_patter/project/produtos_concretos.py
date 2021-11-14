from project.produtos_abstract import Sofa, Cama, Cadeira


class SofaVitoriano(Sofa):
    def deitar(self):
        print('Deitando em um sofá estilo Vitoriano.')

    def sentar(self):
        print('Sentando em um sofá estilo Vitoriano.')


class CamaVitoriana(Cama):
    def deitar(self):
        print('Deitando em uma cama estilo Vitoriano.')


class CadeiraVitoriana(Cadeira):
    def sentar(self):
        print('Sentando em uma cadeira estilo Vitoriano.')


class SofaModerno(Sofa):
    def deitar(self):
        print('Deitando em um sofá estilo Moderno.')

    def sentar(self):
        print('Sentando em um sofá estilo Moderno.')


class CamaModerna(Cama):
    def deitar(self):
        print('Deitando em uma cama estilo Moderno.')


class CadeiraModerna(Cadeira):
    def sentar(self):
        print('Sentando em uma cadeira estilo Moderno.')
