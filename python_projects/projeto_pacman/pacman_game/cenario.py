from typing import List

import pygame
from pygame import Surface
from pygame.font import Font
from pygame.event import Event

from pacman_game.elemento_jogo import ElementoJogo
from pacman_game.constantes import *
from pacman_game.pacman import Pacman
from pacman_game.validador_elemento_movel import ValidadorElementoMovel
from pacman_game.elemento_movel import ElementoMovel
from pacman_game.fantasma import Fantasma


class Cenario(ElementoJogo, ValidadorElementoMovel):
    cor = {0: PRETO, 1: PRETO, 2: AZUL}

    def __init__(self, tamanho: int, fonte: Font, pacman: Pacman):
        self._pacman = pacman
        self._moviveis = []
        self.fonte = fonte
        self._tamanho = tamanho
        self._pontos = 0
        # Estados possíveis 0 -> Jogando, 1 -> Pausado, 2 -> Game-Over e 3 -> Venceu
        self._estado = "JOGANDO"
        self._pause_delay = 0
        self._matrix = MATRIZ
        self._vidas = 3

    def adicionar_elemento_movivel(self, obj: ElementoMovel) -> None:
        self._moviveis.append(obj)

    def pintar_score(self, tela: Surface) -> None:
        pontos_x = 1 * self._tamanho
        pontos_y = 28 * self._tamanho
        img_pontos = self.fonte.render(f"Score: {self._pontos}", True, AMARELO)
        img_vidas = self.fonte.render(f"Vidas {self._vidas}", True, AMARELO)
        tela.blit(img_pontos, (pontos_x, pontos_y))
        tela.blit(img_vidas,  (pontos_x, 0))

    def pintar_linha(self, tela: Surface, numero_linha: int, linha: List[int]) -> None:
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self._tamanho
            y = numero_linha * self._tamanho

            pygame.draw.rect(tela, self.cor[coluna], (x, y, self._tamanho, self._tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, BRANCO, (x + self._tamanho // 2, y + self._tamanho // 2), self._tamanho // 10,
                                   0)

    def pintar(self, tela: Surface) -> None:
        if self._estado == "JOGANDO":
            self.pintar_jogando(tela)
        elif self._estado == "PAUSADO":
            self.pintar_pausado(tela)
        elif self._estado == "GAMEOVER":
            self.pintar_gameover(tela)
        elif self._estado == "VITORIA":
            self.pintar_vitoria(tela)

    def pintar_jogando(self, tela: Surface) -> None:
        for numero_linha, linha in enumerate(self._matrix):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_score(tela)

    def pintar_texto_no_centro(self, tela: Surface, texto: str) -> None:
        texto_img = self.fonte.render(texto, True, AMARELO)
        texto_x = (tela.get_width() - texto_img.get_width()) // 2
        texto_y = (tela.get_height() - texto_img.get_height()) // 2
        tela.blit(texto_img, (texto_x, texto_y))

    def pintar_pausado(self, tela: Surface) -> None:
        self.pintar_jogando(tela)
        self.pintar_texto_no_centro(tela, "P A U S A D O")

    def pintar_gameover(self, tela: Surface) -> None:
        self.pintar_jogando(tela)
        self.pintar_texto_no_centro(tela, "G A M E  O V E R")

    def pintar_vitoria(self, tela: Surface) -> None:
        self.pintar_jogando(tela)
        self.pintar_texto_no_centro(tela, "P A R A B E N S  V O C E  V E N C E U!")

    def get_direcoes(self, linha: int, coluna: int) -> List[int]:
        direcoes = []
        if self._matrix[int(linha - 1)][int(coluna)] != 2:
            direcoes.append(ACIMA)
        if self._matrix[int(linha + 1)][int(coluna)] != 2:
            direcoes.append(ABAIXO)
        if self._matrix[int(linha)][int(coluna - 1)] != 2:
            direcoes.append(ESQUERDA)
        if self._matrix[int(linha)][int(coluna + 1)] != 2:
            direcoes.append(DIREITA)
        return direcoes

    def calcular_regras_jogando(self) -> None:
        for elemento_movel in self._moviveis:
            lin = int(elemento_movel.linha)
            col = int(elemento_movel.coluna)
            lin_intencao = int(elemento_movel.linha_intencao)
            col_intencao = int(elemento_movel.coluna_intencao)
            direcoes = self.get_direcoes(lin, col)
            if len(direcoes) >= 3:
                elemento_movel.esquina(direcoes)
            if (isinstance(elemento_movel, Fantasma) and elemento_movel.linha == self._pacman.linha
                    and elemento_movel.coluna == self._pacman.coluna):
                self._vidas -= 1
                if self._vidas <= 0:
                    self._estado = "GAMEOVER"
                else:
                    self._pacman.linha = 1
                    self._pacman.coluna = 1
            else:
                if (0 <= col_intencao < 28 and 0 <= lin_intencao < 29
                        and self._matrix[lin_intencao][col_intencao] != 2):
                    elemento_movel.aceitar_movimento()
                    if isinstance(elemento_movel, Pacman) and self._matrix[lin][col] == 1:
                        self._pontos += 1
                        self._matrix[lin][col] = 0
                        self.verificar_se_vitoria()
                else:
                    elemento_movel.recusar_movimento(direcoes)

    def calcular_regras_pausado(self) -> None:
        pass

    def calcular_regras_gameover(self) -> None:
        pass

    def verificar_se_vitoria(self):
        if self._pontos >= POINTS:
            self._estado = "VITORIA"

    def calcular_regras(self) -> None:
        if self._estado == "JOGANDO":
            self.calcular_regras_jogando()
        elif self._estado == "PAUSADO":
            self.calcular_regras_pausado()
        elif self._estado == "GAMEOVER":
            self.calcular_regras_gameover()

    def processar_eventos(self, eventos: List[Event]) -> None:
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self._estado == "JOGANDO":
                        self._estado = "PAUSADO"
                    else:
                        self._estado = "JOGANDO"
