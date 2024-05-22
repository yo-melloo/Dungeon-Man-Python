'''
DUNGEON MAN 1.5 - 2024 ver
Author: Gustavo Mello
Description: RPG Experimental Backend Game
'''

import spawner as Sp
import market
from interations import Interface as Ui
from interations import Player

Ui.play()
playername = Ui.setPlayerName()
playerclass = Ui.setPlayerClass()
player = Player(playername, playerclass)
player.summarize()

# Etapas e Funcionalidades do Jogo:
# Etapa 1 - Criar personagem -- OK
    # Sistema de Classes -- OK
    # Sistema de Atributos -- OK
# Etapa 2 - Lutar contra um inimigo
    # Sistema de Spawn de Inimigos
    # Sistema de Luta
    # Sistema de especiais
    # Sistema de fuga
# Etapa 3 - Subir de nível
    # Funcionalidades interativas com Sis. de Atributos
    # Multiplicador de dificuldade
# Etapa 4 - Comprar items
    # Sistema de loja
    # Sistema de economia
    # Sistema de troca