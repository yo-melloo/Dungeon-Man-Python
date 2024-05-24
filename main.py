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
playeralive = True
#playerdesc.summarize() # -- Resume personagem

# PARTE 1: ENTRAR NA DUNGEON
level = 1
sorte = 0
stack = 0

def playerAttack():
    mob = playeractions.attack(mob, player, sorte, stack) # -- mob sofre dano
    stack += Player.stackar(mob, player, stack) # -- player stacka
    sorte = random.randint(1,3) # -- sorte do player muda a cada turno


#Mainloop:
while (playeralive == True and level <= 32): # 'desce na Dungeon até nivel 32 enquanto estiver vivo
        mob = Mob.spawn(level, sorte) # spawna o mob conforme nivel
        
        while (playeralive == True): # enquanto personagem estiver vivo, é possível jogar
            print(f"#### LEVEL {level} ####")
                       
            # -- TURNO DO JOGADOR:
            Ui.enemyInfo(mob, level) # -- Exibe o status do inimigo
            res = Player.gui() # -- Recebe escolha do jogador
            if res == 1:
                playerAttack()
            if res == 2:
                Player.backpack()
            if res == 3:
                #Player.specialAttack() # -- ainda não criado
                print('você não tem ataques especiais (ainda)')
                pass
            if res == 4:
                #Player.run(mob)
                if player['spd'] <= mob['spd']:
                    print('não é possível fugir desse monstro, ele é mais rápido')
                    player = Mob.attack(mob, player)
                else:
                    print('Parabéns, você pulou esse monstro')
                    level += 1
                    break
            
            
            # -- TURNO DO MOB:
            print(f">> {mob['name']} atacou {player['name']}")
            player = Mob.attack(mob, player)
            Player.stats()
            if player['hp'] <= 0:
                playeralive = False
                
while()
if playeralive == False:
    extraLife -= 1
                
            
    
    
# PARTE 2: ENCONTRAR O MERCADOR

# PARTE 3: LUTAR CONTRA O PRIMEIRO MONSTRO

# PARTE 4: LER PRIMEIRO TRECHO DE HISTÓRIA

