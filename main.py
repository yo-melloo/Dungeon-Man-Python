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
    # Sistema de Luta -> em estágio inicial
    # Sistema de especiais
    # Sistema de fuga
# Etapa 3 - Subir de nível
    # Funcionalidades interativas com Sis. de Atributos
    # Multiplicador de dificuldade
# Etapa 4 - Comprar items
    # Sistema de loja
    # Sistema de economia
    # Sistema de troca


#from spawner import Mob
import market
from interations import Interface as Ui
from interations import Game
from interations import Player
#import random
#import time

# PARTE 1 --- START!
Ui.play() # -- Dá play no jogo
playername = Player.setPlayerName() # -- recebe nome para personagem
playerclass = Player.setPlayerClass() # -- recebe classe para personagem
jogador = Player(playername, playerclass) # -- inicia personagem
level = 0
inventario = []
jogador.summarize(level, inventario) # -- Resume personagem - Aqui tentei usar os conceitos de POO novos que aprendi, mas prevejo que não vou usar muita coisa

## menu principal ##
def mainMenu():
    global level
    menuString = f'''
    --MENU PRINCIPAL--
    
#######[ LEVEL {level} ]########

(SELECIONE UMA AÇÃO):
- (D) DESCER NA DUNGEON
- (L) LOJA DE ITENS
- (S) SAIR DO JOGO 

--> '''
    playerChoice = input(menuString).upper()
    if (playerChoice == "D"):
        level = Game.descerDungeon(level, playername, jogador)
    elif (playerChoice == "L"):
        print('loja ainda não foi construída')
        pass
    elif (playerChoice == "S"):
            print("------------------------------\n*** [encerrando jogo...] ***\n------------------------------")
            exit()

# PARTE 2 --- História
# aqui vai ser criado uma função que exibe trechos do texto da história conforme o nível do jogador (Loop)
#

# PARTE 3 --- Pausa / Loja
# aqui vai ser criado uma função onde o jogador pode comprar, trocar e vender itens do seu inventário
#


# PARTE 4 --- Looping de Dungeon
# Aqui vai loop que spawna e cria sistema de combate com mobs


while level < 10:
    mainMenu()
