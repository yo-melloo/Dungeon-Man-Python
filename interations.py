'''
DUNGEON MAN 1.5 - 2024 ver
Author: Gustavo Mello
Description: DUNGEON MAN USER INTERACTIONS

'''

import random
from spawner import Mob

# Criar Comunicadores
# Criar Gerador de Personagem e sistema de Level Up

class Interface:
    def __init__(self) -> None:
        pass
    def play():
        start = input('> Deseja iniciar o jogo? (S/N): ')
        if (start.upper() == "N" or start.upper() == "NÃO"):
            print("------------------------------\n*** encerrando jogo... ***\n------------------------------")
            exit()
        
        #newgame = input('> Deseja continuar da onde parou? (S/N)') # -- Modo de Carregar progresso (se for possível)

        print('\n\n-----------------------------------\n### Bem-vindo a Dungeon Man ###')
        print('--- ver 1.5 beta - set 2024 ---\n-----------------------------------')
    
    def enemyInfo(mob):
        return(f"> {mob['name']}\n> HP: {mob['hp']}\n> ATK: {mob['atk']}\n> DEF: {mob['def']}\n> SPD: {mob['spd']}")
    
    
    def descerDungeon(level, playername, jogador):
        playerAlive = True
        mobAlive = True
        level += 1
        luck = random.randrange(0,3)   
        mob = Mob.spawn(level, luck) # -- Spawna o mob, conforme o level e sorte do jogador
        
        print(f'''-------------------------
--> {playername.upper()} DESCEU NA DUNGEON **
-------------------------''')
        
        print(f"\n#######[LEVEL {level}]########")
        
        print(f"\n{mob['name'].upper()} FOI ENCONTRADO!")
        
        playerChoices = '''________________________

[ ] (A) ATACAR 
[ ] (I) INVENTÁRIO 
[ ] (F) FUGIR 

(  ) > SELECIONE UMA AÇÃO: '''

        while (playerAlive == True and mobAlive == True):
            print(f'''
-------------------------

{playername.capitalize()}  X   {mob['name'].capitalize()}
{jogador.playerHP}HP	    {mob['hp']}HP
{jogador.playerATK}ATK	    {mob['atk']}ATK
{jogador.playerDEF}DEF	    {mob['def']}DEF
{jogador.playerSPD}VEL	    {mob['spd']}VEL
''')
            while True:
            # -- turno do jogador:
                playerAction = input(playerChoices).upper()
                
                if (playerAction == "A"):
                    mob['hp'] = Player.attack(jogador, mob)
                    if (mob['hp'] == 0): 
                        mobAlive = False
                    break
                #elif (playerAction == "I"):
                #elif (playerAction == "F"):
                else:
                    print('-> comando inválido\n')
            
            # -- turno do Mob
            if (mobAlive == True):
                #print(jogador)
                Mob.attack(mob, jogador)
                
            #return level



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
        playerName = input('\n( * ) > Digite um nome para seu personagem: ').capitalize()
        print(f'\n-----------------------------------\n\n*** você criou {playerName} ***\n\n> Defina uma classe para {playerName} a seguir:\n')
        return playerName
    
    def setPlayerClass():
        line = '----------------------------\n' # string útil para acelerar código
        playerClassWarrior = {'class':'Guerreiro','hp':280,'atk':80,'def':45,'spd':20,'spc_attack':'NONE', 'desc':'bom em ataque e defesa'}
        playerClassShooter = {'class':'Atirador','hp':200,'atk':95,'def':30,'spd':35,'spc_attack':'NONE', 'desc':'excelente em ataque e furtividade'}
        playerClassMage = {'class':'Mago','hp':220,'atk':70,'def':40,'spd':35,'spc_attack':'Fire Ball', 'desc':'excelente em jogadas estratégicas'}
        playerClassDemon = {'class':'Demônio','hp':310,'atk':90,'def':55,'spd':40,'spc_attack':'Diabolic Punch', 'desc':'excelente em lutas'}
        
        print(line)
        print('### Classes ###\n')
        print(f'CLASSE: {playerClassWarrior["class"]}\nDESCRIÇÃO: {playerClassWarrior["desc"]}\n\n_____(ATRIBUTOS)_____\n\nSAÚDE: {playerClassWarrior["hp"]}\nATAQUE: {playerClassWarrior["atk"]}\nDEFESA: {playerClassWarrior["def"]}\nVELOCIDADE: {playerClassWarrior["spd"]}\n')
        print(line)
        print(f'CLASSE: {playerClassShooter["class"]}\nDESCRIÇÃO: {playerClassShooter["desc"]}\n\n_____(ATRIBUTOS)_____\n\nSAÚDE: {playerClassShooter["hp"]}\nATAQUE: {playerClassShooter["atk"]}\nDEFESA: {playerClassShooter["def"]}\nVELOCIDADE: {playerClassShooter["spd"]}\n')
        print(line)
        print(f'CLASSE: {playerClassMage["class"]}\nDESCRIÇÃO: {playerClassMage["desc"]}\n\n_____(ATRIBUTOS)_____\n\nSAÚDE: {playerClassMage["hp"]}\nATAQUE: {playerClassMage["atk"]}\nDEFESA: {playerClassMage["def"]}\nVELOCIDADE: {playerClassMage["spd"]}\n')
        print(line)
        print(f'CLASSE: {playerClassDemon["class"]}\nDESCRIÇÃO: {playerClassMage["desc"]}\n\n_____(ATRIBUTOS)_____\n\nSAÚDE: {playerClassDemon["hp"]}\nATAQUE: {playerClassDemon["atk"]}\nDEFESA: {playerClassDemon["def"]}\nVELOCIDADE: {playerClassDemon["spd"]}\n')
        print(line)

        while (True):
            playerInputChoose = input('( * ) > Digite o nome da classe escolhida: ')
            
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
    
    def summarize(self, level, inventario): # -- Função experimental para uso do ".self"
        
        print(f'\n--------------------##--------------------##\n\n-- Olá, meu nome é {self.playername}, será um prazer te acompanhar nessa jornada no incível mundo de Dungeon Man!\n-- Eu sou um {self.playerclass}, isso significa que sou {self.playerDesc}')        
        print(f'--> Nivel do {self.playername}: {level}')
        if inventario == []: 
            print("--> Inventário [vazio]\n\n--------------------##--------------------##\n")
        else:
            print(f'--> Inventário [{inventario}]\n\n--------------------##--------------------##\n')


    def attack(self, mob):
       #if id == 1:
        mobdef = mob['def']
        mobhp = mob['hp']
        mobhpe = mobhp

        playerDMG = self.playerATK - mobdef
        mobhp -= playerDMG
        if (mobhp < 0): mobhp = 0
        
        attackString = f'''
--------------------------------------
    
    --> {self.playername.capitalize()} atacou {mob['name'].capitalize()}! <--

    {mob['name']} HP: {mobhpe} -> {mobhp} ({playerDMG} de Dano)

--------------------------------------

'''
        print(attackString)
        
        return mobhp

    #elif id == 2:
    #    autorataquemob = autor['atk']
    #    alvodefesaplayer = alvo.playerDEF
    #    alvohpplayer = alvo.playerHP
    #    
    #    danomob = autorataquemob - alvodefesaplayer
    #    alvohpplayer -= danomob
    #    return alvohpplayer
    #else:
    #    return "erro, argumentos inválidos"