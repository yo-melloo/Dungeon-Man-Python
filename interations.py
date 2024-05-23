'''
DUNGEON MAN 1.5 - 2024 ver
Author: Gustavo Mello
Description: DUNGEON MAN USER INTERACTIONS

'''

# Criar Comunicadores
# Criar Gerador de Personagem e sistema de Level Up

class Interface:
    def __init__(self) -> None:
        pass
    def play():
        start = input('> Deseja iniciar o jogo? (S/N): ')
        if (start.upper() == "N" or start == "NÃO"):
            print("*** encerrando jogo... ***")
            exit()
        
        #newgame = input('> Deseja continuar da onde parou? (S/N)') # -- Modo de Carregar progresso (se for possível)

        print('### Bem-vindo a Dungeon Man ###')
        print('--- ver 1.5 - mai 2024 ---')
    
    def enemyInfo(mob):
        
        #### LEVEL 00 ####
        Inimigo: mob['name']
        HP: mob['hp'] // ATK: mob['atk'] // DEF: mob['def'] // VEL: mob['spd']
        SPECIAL: mob['spc_attack']

        (INFO) mob['desc']
        ------------------------
        [F] ATACAR
        [B] INVENTÁRIO
        [S] ESPECIAL
        [Q] FUGIR

        > DIGITE UM COMANDO A SER EXECUTADO: 


class Player:
    def __init__(self, playername, playerclass) -> None:
        self.playername = playername
        self.playerAttributes = playerclass
        self.playerclass = playerclass['class']
        self.playerHP = playerclass['hp']
        #self.playerMaxHP = playerclass['max_hp']
        self.playerATK = playerclass['atk']
        self.playerDEF = playerclass['def']
        self.playerSPD = playerclass['spd']
        self.playerSPC = playerclass['spc_attack']
        self.playerDesc = playerclass['desc']
        pass
    
    def setPlayerName():
        playerName = input('> Digite um nome para seu personagem: ').capitalize()
        print(f'*** você criou {playerName} ***\n> Defina uma classe para {playerName} a seguir:')
        return playerName
    
    def setPlayerClass():
        line = '----------------------------\n' # string útil para acelerar código
        playerClassWarrior = {'class':'Guerreiro','hp':280,'atk':80,'def':45,'spd':20,'spc_attack':'NONE', 'desc':'bom em ataque e defesa'}
        playerClassShooter = {'class':'Atirador','hp':200,'atk':95,'def':30,'spd':35,'spc_attack':'NONE', 'desc':'excelente em ataque e furtividade'}
        playerClassMage = {'class':'Mago','hp':220,'atk':75,'def':40,'spd':35,'spc_attack':'Fire Ball', 'desc':'excelente em jogadas estratégicas'}
        playerClassDemon = {'class':'Demônio','hp':310,'atk':90,'def':55,'spd':40,'spc_attack':'Diabolic Punch', 'desc':'excelente em lutas'}
        
        print('\n### Classes ###\n')
        print(line)
        print(f'CLASSE: {playerClassWarrior["class"]}\nDESCRIÇÃO:{playerClassWarrior["desc"]} \n(ATRIBUTOS):\nSAÚDE: {playerClassWarrior["hp"]}\nATAQUE: {playerClassWarrior["atk"]}\nDEFESA: {playerClassWarrior["def"]}\nVELOCIDADE: {playerClassWarrior["spd"]}\n')
        print(line)
        print(f'CLASSE: {playerClassShooter["class"]}\nDESCRIÇÃO:{playerClassShooter["desc"]} \n(ATRIBUTOS):\nSAÚDE: {playerClassShooter["hp"]}\nATAQUE: {playerClassShooter["atk"]}\nDEFESA: {playerClassShooter["def"]}\nVELOCIDADE: {playerClassShooter["spd"]}\n')
        print(line)
        print(f'CLASSE: {playerClassMage["class"]}\nDESCRIÇÃO:{playerClassMage["desc"]} \n(ATRIBUTOS):\nSAÚDE: {playerClassMage["hp"]}\nATAQUE: {playerClassMage["atk"]}\nDEFESA: {playerClassMage["def"]}\nVELOCIDADE: {playerClassMage["spd"]}\n')
        print(line)
        print(f'CLASSE: {playerClassDemon["class"]}\nDESCRIÇÃO:{playerClassMage["desc"]} \n(ATRIBUTOS):\nSAÚDE: {playerClassDemon["hp"]}\nATAQUE: {playerClassDemon["atk"]}\nDEFESA: {playerClassDemon["def"]}\nVELOCIDADE: {playerClassDemon["spd"]}\n')
        print(line)

        while (True):
            playerInputChoose = input('> Digite o nome da classe escolhida: ')
            
            if (playerInputChoose.capitalize() == playerClassWarrior['class']):
                playerClass = playerClassWarrior
                break
            elif (playerInputChoose.capitalize() == playerClassShooter['class']):
                playerClass = playerClassShooter
                break
            elif (playerInputChoose.capitalize() == playerClassMage['class']):
                playerClass = playerClassMage
                break
            elif (playerInputChoose.capitalize() == playerClassDemon['class']):
                playerClass = playerClassDemon
                break
            else:
                print('> digite o nome correto de uma das CLASSES acima')
        
        return playerClass
    
    def summarize(self): # -- Função experimental para uso do ".self"
        print(f'\n-- Olá, meu nome é {self.playername}, será um prazer te acompanhar nessa jornada no incível mundo de Dungeon Man!\n-- Eu sou um {self.playerclass}, isso significa que sou {self.playerDesc}')
    
    def attack(self, mob, player, sorte, stack):
        #mobHP = mob['hp']
        mobDEF = mob['def']
        playerATK = player['atk']
        playerCRIT = int(player['atk'] * (sorte / 10))
        if (stack >= 100):
            dano = playerATK + playerCRIT - mobDEF
            if (dano <= 0): 
                dano = 0
                print('*** DANO ZERO ***')
            else:
                print('*** DANO CRÍTICO ***')    
        else:
            dano = playerATK - mobDEF
            if (dano <= 0): 
                dano = 0
                print('*** DANO ZERO ***')
            else:
                print(f"*** {dano}DMG de DANO ***")
        mob['hp'] -= dano
        if mob['hp'] < 0:
            mob['hp'] = 0
        return mob
    
    def stackar(mob, player, stack):
        if stack == 100:
            stack = 0
        print(f'\n\nstacks atual: >>> {stack} <<<')
        #mobHP = mob['hp']
        mobDEF = mob['def']
        playerATK = player['atk']
        dano = playerATK - mobDEF
        if (dano <= 0): dano = 0
        print(f"estacando: {dano}dmg\n\n")
        return dano
               