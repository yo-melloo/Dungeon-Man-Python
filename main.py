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
import random

# PARTE 1 --- START!
Ui.play() # -- Dá play no jogo
playername = Player.setPlayerName() # -- recebe nome para personagem
player = Player.setPlayerClass() # -- recebe classe para personagem
playeractions = Player(playername, player) # -- inicia personagem
playerAlive = True
#playerdesc.summarize() # -- Resume personagem

# PARTE 1: ENTRAR NA DUNGEON

# PARTE 2: ENCONTRAR O MERCADOR

# PARTE 3: LUTAR CONTRA O PRIMEIRO MONSTRO

# PARTE 4: LER PRIMEIRO TRECHO DE HISTÓRIA

level = 1
sorte = 0
stack = 0
playeralive = True

#loop de luta:
while (playeralive == True and level <= 32): # condições para 'descer na Dungeon'
    print(f"Level: {level} - SORTE {sorte}")
    mob = Mob.spawn(level, sorte) # -- Spawna o mob, conforme o level e sorte do jogador
    Ui.enemyInfo(mob)
    if (input() != ""):
        playeralive = False
    else:
        stack += Player.stackar(mob, player, stack)
        sorte = random.randint(1,3)
        level += 1

while True:
    mob = playeractions.attack(mob, player, sorte, stack)
    if (mob['hp'] <= 0):
        break

    print(f"*** {mob['name']} contra-ataca: ***")
    print(f'>> player ANTES: {player}')
    player = Mob.attack(mob, player, stack)
    print(f'>> player DEPOIS: {player}')
    input()
    if (player['hp'] <= 0):
        break