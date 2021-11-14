import pygame
from pygame import Surface
from pacman_game.constantes import *
from pacman_game.pacman import Pacman
from pacman_game.cenario import Cenario
from pacman_game.fantasma import Fantasma

pygame.init()

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), FLAGS)
fonte = pygame.font.SysFont("arial", 20, True, False)

if __name__ == '__main__':
    size = LARGURA_TELA // 30
    pacman = Pacman(size)
    blinky = Fantasma(VERMELHO, size)
    inky = Fantasma(CIANO, size)
    clyde = Fantasma(LARANJA, size)
    pinky = Fantasma(ROSA, size)
    cenario = Cenario(size, fonte, pacman)
    cenario.adicionar_elemento_movivel(pacman)
    cenario.adicionar_elemento_movivel(blinky)
    cenario.adicionar_elemento_movivel(inky)
    cenario.adicionar_elemento_movivel(clyde)
    cenario.adicionar_elemento_movivel(pinky)

    while True:
        # Calcular a regra
        pacman.calcular_regras()
        blinky.calcular_regras()
        inky.calcular_regras()
        clyde.calcular_regras()
        pinky.calcular_regras()
        cenario.calcular_regras()

        # Pintar a tela
        #pygame.time.Clock().tick(10)
        pygame.time.delay(120)
        tela.fill(PRETO)
        cenario.pintar(tela)
        pacman.pintar(tela)
        blinky.pintar(tela)
        inky.pintar(tela)
        clyde.pintar(tela)
        pinky.pintar(tela)
        pygame.display.update()

        eventos = pygame.event.get()
        pacman.processar_eventos(eventos)
        cenario.processar_eventos(eventos)
