from typing import List

import pygame
from pygame import Surface
from pygame.event import Event

from pacman_game.elemento_movel import ElementoMovel
from pacman_game.elemento_jogo import ElementoJogo
from pacman_game.constantes import *


class Pacman(ElementoJogo, ElementoMovel):

    def __init__(self, tamanho: int):
        self._coluna = 1
        self._linha = 1
        self._centro_x = 400
        self._centro_y = 300
        self._tamanho = tamanho
        self._vel_x = 0
        self._vel_y = 0
        self._raio = self._tamanho // 2
        self._abertura = 0
        self._vel_abertura = VELOCIDADE_ABERTURA
        self._orientacao = 1
        self.coluna_intencao = self._coluna
        self.linha_intencao = self._linha

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

    def calcular_regras(self) -> None:
        self.coluna_intencao = self._coluna + self._vel_x
        self.linha_intencao = self._linha + self._vel_y
        self._centro_x = int(self._coluna * self._tamanho + self._raio)
        self._centro_y = int(self._linha * self._tamanho + self._raio)

    def pintar(self, tela: Surface):
        # Desenhar corpo do pacman_game
        pygame.draw.circle(tela, AMARELO, (self._centro_x, self._centro_y), self._raio, 0)
        self._abertura += self._vel_abertura
        if self._abertura >= self._raio:
            self._vel_abertura = -VELOCIDADE_ABERTURA
        if self._abertura <= 0:
            self._vel_abertura = VELOCIDADE_ABERTURA

        canto_boca = (self._centro_x, self._centro_y)
        labio_superior = (self._centro_x + self._raio, self._centro_y - self._raio + self._abertura)
        labio_inferior = (self._centro_x + self._raio, self._centro_y + self._raio - self._abertura)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        olho_x = int(self._centro_x + self._raio / 3)
        olho_y = int(self._centro_y - self._raio * 0.7)
        olho_raio = int(self._raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def processar_eventos(self, eventos: List[Event]) -> None:
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self._vel_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self._vel_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    self._vel_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self._vel_y = VELOCIDADE
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self._vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self._vel_x = 0
                if e.key == pygame.K_UP:
                    self._vel_y = 0
                elif e.key == pygame.K_DOWN:
                    self._vel_y = 0

    def aceitar_movimento(self) -> None:
        self._linha = self.linha_intencao
        self._coluna = self.coluna_intencao

    def recusar_movimento(self, direcoes: List[int]) -> None:
        self.linha_intencao = self._linha
        self.coluna_intencao = self._coluna

    def esquina(self, direcoes: List[int]) -> None:
        pass
