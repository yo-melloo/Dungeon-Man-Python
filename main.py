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


# PARTE 2 --- História
# aqui vai ser criado uma função que exibe trechos do texto da história conforme o nível do jogador (Loop)
#

# PARTE 3 --- Pausa / Loja
# aqui vai ser criado uma função onde o jogador pode comprar, trocar e vender itens do seu inventário
#


# PARTE 4 --- Looping de Dungeon
# Aqui vai loop que spawna e cria sistema de combate com mobs
'''
level = 1

while (playerAlive == True and level <= 32):
    playerluck = random.randint(1,3)
    print(f"Level: {level} - SORTE {playerluck}")
    mob = Mob.spawn(level, playerluck) # -- Spawna o mob, conforme o level e sorte do jogador
    Ui.enemyInfo(mob)
    if (input() != ""):
        playerAlive = False
    else:
        level += 1


# -- Sistema de Dano Crítico (prototipo)
#sorte = 2
#mob = Mob.spawn(1, sorte)
crit = int(player['atk'] * (sorte / 10))
dano = int(player['atk'] + crit)
print(f"o seu dano crítico, causaria {crit} dmg de dano adicional no {mob['name']}, um total  de {dano}dmg de dano!")
'''

sorte = 2
stack = 0
mob = Mob.spawn(1, sorte)
print(f'>> MOB SPAWNADO: {mob}')
while True:
    print(f'*** {playername} iniciou ataque!')
    print(f'> mob ANTES: {mob}')
    mob = playeractions.attack(mob, player, sorte, stack)
    stack += Player.stackar(mob, player, stack)
    print(f'> mob DEPOIS: {mob}')
    input()
    if (mob['hp'] <= 0):
        break

    print(f"*** {mob['name']} contra-ataca: ***")
    print(f'>> player ANTES: {player}')
    player = Mob.attack(mob, player, stack)
    print(f'>> player DEPOIS: {player}')
    input()
    if (player['hp'] <= 0):
        break