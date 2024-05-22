'''
DUNGEON MAN 1.5 - 2024 ver
Author: Gustavo Mello
Description: RPG Experimental Backend Game
'''

# Etapas e Funcionalidades do Jogo:
# Etapa 1 - Criar personagem -- OK
    # Sistema de Classes -- OK
    # Sistema de Atributos -- OK
# Etapa 2 - Lutar contra um inimigo
    # Sistema de Spawn de Inimigos -- OK
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


from spawner import Mob
import market
from interations import Interface as Ui
from interations import Player

# PARTE 1 --- START!
Ui.play() # -- Dá play no jogo
playername = Player.setPlayerName() # -- recebe nome para personagem
playerclass = Player.setPlayerClass() # -- recebe classe para personagem
player = Player(playername, playerclass) # -- inicia personagem
#player.summarize() # -- Resume personagem


# PARTE 2 --- História
# aqui vai ser criado uma função que exibe trechos do texto da história conforme o nível do jogador (Loop)
#

# PARTE 3 --- Pausa / Loja
# aqui vai ser criado uma função onde o jogador pode comprar, trocar e vender itens do seu inventário
#


# PARTE 4 --- Looping de Dungeon
# Aqui vai loop que spawna e cria sistema de combate com mobs
mob = Mob.spawn(1, 1) # -- Spawna o mob, conforme o level e sorte do jogador
#Ui.enemyInfo(mob)