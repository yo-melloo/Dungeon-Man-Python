'''
DUNGEON MAN 1.5 - 2024 ver
Author: Gustavo Mello
Description: RPG Experimental Backend Game
'''

import spawner as Sp
import market
import interations as ui
import random

level = random.randint(1,32)
luck = random.randint(0,3)
print(f'sorte: {luck}')
print(f'entrando no level {level}')

npcMob = Sp.Mob.spawn(level, luck)
#print(type(npcMob))
print(f"*** Você encontrou um {npcMob['name']}")


# Etapas e Funcionalidades do Jogo:
# Etapa 1 - Criar personagem
    # Sistema de Classes
    # Sistema de Atributos
# Etapa 2 - Lutar contra um inimigo
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