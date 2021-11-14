from typing import List
import random

import pygame
from pygame import Surface
from pygame.event import Event

from pacman_game.constantes import *
from pacman_game.elemento_jogo import ElementoJogo
from pacman_game.elemento_movel import ElementoMovel


class Fantasma(ElementoJogo, ElementoMovel):

    def __init__(self, cor, tamanho):
        self._coluna = 15
        self._linha = 14
        self.linha_intencao = self._linha
        self.coluna_intencao = self._coluna
        self._velocidade = VELOCIDADE
        self._direcao = ABAIXO
        self._direcao_old = self._direcao
        self._tamanho = tamanho
        self._cor = cor

    @property
    def linha(self) -> int:
        return self._linha

    @linha.setter
    def linha(self, value: int) -> None:
        self._linha = value

    @property
    def coluna(self) -> int:
        return self._coluna

    @coluna.setter
    def coluna(self, value: int) -> None:
        self._coluna = value

    def pintar(self, tela: Surface) -> None:
        fatia = self._tamanho // 8
        px = int(self._coluna * self._tamanho)
        py = int(self._linha * self._tamanho)
        contorno = [(px, py + self._tamanho),
                    (px + fatia * 1, py + fatia * 2),
                    (px + fatia * 2.7, py + fatia // 2),
                    (px + fatia * 4.5, py),
                    (px + fatia * 5.5, py),
                    (px + fatia * 7.2, py + fatia // 2),
                    (px + fatia * 8, py + fatia * 2),
                    (px + self._tamanho, py + self._tamanho)]
        pygame.draw.polygon(tela, self._cor, contorno, 0)

        olho_raio_ext = fatia
        olho_raio_int = fatia // 2

        olho_e_x = int(px + fatia * 2.7)
        olho_e_y = int(py + fatia * 2.5)

        olho_d_x = int(px + fatia * 6.5)
        olho_d_y = int(py + fatia * 2.5)

        pygame.draw.circle(tela, BRANCO, (olho_e_x, olho_e_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, PRETO, (olho_e_x, olho_e_y), olho_raio_int, 0)
        pygame.draw.circle(tela, BRANCO, (olho_d_x, olho_d_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, PRETO, (olho_d_x, olho_d_y), olho_raio_int, 0)

    def calcular_regras(self) -> None:
        if self._direcao == ACIMA:
            self.linha_intencao -= self._velocidade
        elif self._direcao == ABAIXO:
            self.linha_intencao += self._velocidade
        elif self._direcao == ESQUERDA:
            self.coluna_intencao -= self._velocidade
        elif self._direcao == DIREITA:
            self.coluna_intencao += self._velocidade

    def mudar_direcao(self, direcoes: List[int]) -> None:
        self._direcao = random.choice(direcoes)

    def aceitar_movimento(self) -> None:
        self._linha = self.linha_intencao
        self._coluna = self.coluna_intencao

    def recusar_movimento(self, direcoes: List[int]) -> None:
        self.linha_intencao = self._linha
        self.coluna_intencao = self._coluna
        self.mudar_direcao(direcoes)

    def esquina(self, direcoes: List[int]) -> None:
        self.mudar_direcao(direcoes)

    def processar_eventos(self, eventos: List[Event]) -> None:
        pass
