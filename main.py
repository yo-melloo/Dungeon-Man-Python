'''
DUNGEON MAN 1.5 - 2024 ver
Author: Gustavo Mello
Description: RPG Experimental Backend Game
'''

# Etapas e Funcionalidades do Jogo:
# Etapa 1 - Criar personagem -- OK
    # Sistema de Classes -- OK
    # Sistema de Atributos -- finalizar
# Etapa 2 - Lutar contra um inimigo
    # Sistema de Spawn de Inimigos -- OK
    # Sistema de Luta -- Consertar
    # Sistema de Dano critico -- consertar
    # Sistema de especiais
    # Sistema de fuga -- OK
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
Ui.play()
playername = Player.setPlayerName()
player = Player.setPlayerClass()
playeractions = Player(playername, player)
playeralive = True

# PARTE 2 --- RESUMINDO CODIGO
def playerAttack(mob, stack, luck):
    stack += player['atk'] - mob['def']
    mob = playeractions.attack(mob, player, luck, stack) 
    if stack > 100: stack = 0  
    luck = random.randint(0,3) 
    print("------------------------")
    return stack

def mainLoop(playeralive, level, luck, player, stack, extraLife, playername):
    while (playeralive == True and level <= 32):
            luck = random.randint(0,3)
            mob = Mob.spawn(level, luck) 
            mobalive = True
            print(f"\n##################\n#### LEVEL {level} ####\n##################")
            print(F"\n>>> {mob['name']} APARECEU!\n--------------------------")
            
            while (playeralive == True and mobalive == True): 
                Player.stats(player, playername)
                print(f"###### vs. ######")
                Ui.enemyInfo(mob, level)
                # -- TURNO DO JOGADOR:
                
                res = Player.gui(stack)
                if res == 1:
                    print(f">> {playername} atacou {mob['name']}")
                    luck = random.randint(0,3)
                    stack = playerAttack(mob, stack, luck)
                    if mob['hp'] <= 0:
                        print(f"\n*** {mob['name']} MORTO ***")
                        mobalive = False
                        print(f"*** {playername} PASSOU DE FASE! ***")
                        level += 1
                        print(f"**** fase {level - 1} >>> fase {level} ****")
                        print('------------------------')
                        break
                    print('------------------------')
                if res == 2:
                    print('------------------------')
                    Player.backpack()
                if res == 3:
                    print('------------------------')
                    #Player.specialAttack() # -- ainda não criado
                    print('você não tem ataques especiais (ainda)')
                if res == 4:
                    print('------------------------')
                    #Player.run(mob)
                    if player['spd'] <= mob['spd']:
                        print(f">> não é possível fugir desse monstro, ele é mais rápido\n* {mob['name']} te golpeou na tentativa de fuga *")
                        player = Mob.attack(mob, player, 0, playername)
                        if player['hp'] <= 0:
                            print(f'\n***** {playername} MORTO *****')
                            playeralive = False
                            extraLife -= 1
                            break
                    else:
                        print('Parabéns, você pulou esse monstro')
                        print('------------------------')
                        level += 1
                        break
                
                
                # -- TURNO DO MOB:
                print(f">> {mob['name']} atacou {playername}")
                player = Mob.attack(mob, player, 0, playername)
                if player['hp'] <= 0:
                    print(f'\n***** {playername} MORTO *****')
                    playeralive = False
                    extraLife -= 1
                    
    stats = [level, extraLife]
    return stats  


# PARTE 1: ENTRAR NA DUNGEON
level = 1
luck = random.randint(0,3)
stack = random.randint(0, 100)
extraLife = 3
playerBACK = player
print("\n")
             
while(extraLife > 0 or level <= 32):
    stats = mainLoop(playeralive, level, luck, player, stack, extraLife, playername)
    extraLife = stats[1]
    level = stats[0]
    
    if (extraLife <= 0):
        print("GAME OVER!")
        input()
        break
    elif (level >= 32): 
        print("PARABENS, VOCE ZEROU O JOGO")
        break
    else:
        print(F"VOCÊ TEM MAIS {extraLife} CHANCES, TENTE NOVAMENTE")
        player = playerBACK
    
    
# PARTE 2: ENCONTRAR O MERCADOR

# PARTE 3: LUTAR CONTRA O PRIMEIRO MONSTRO

# PARTE 4: LER PRIMEIRO TRECHO DE HISTÓRIA

