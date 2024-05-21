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
    def start():
        pass

class Player:
    def __init__(self, playerName) -> None:
        self.playerName = playerName
        #pass
    
    # Criar Personagem: ---
    def setClass():
        playerClassWarrior = {'class':'Guerreiro','hp':280,'atk':80,'def':45,'spd':20,'spc_attack':'NONE'}
        playerClassShooter = {'class':'Atirador','hp':200,'atk':95,'def':30,'spd':35,'spc_attack':'NONE'}
        playerClassMage = {'class':'Mago','hp':220,'atk':70,'def':40,'spd':35,'spc_attack':'Fire Ball'}
        playerClassDemon = {'class':'Demônio','hp':310,'atk':90,'def':55,'spd':40,'spc_attack':'Diabolic Punch'}
        
        print('\n### Classes ###\n')
        print(f'CLASSE: {playerClassWarrior["class"]}\nDESCRIÇÃO: \nATRIBUTOS:\nSAÚDE: {playerClassWarrior["hp"]}\nATAQUE: {playerClassWarrior["atk"]}\nDEFESA: {playerClassWarrior["def"]}\nVELOCIDADE: {playerClassWarrior["spd"]}\n')
        print(f'CLASSE: {playerClassShooter["class"]}\nDESCRIÇÃO: \nATRIBUTOS:\nSAÚDE: {playerClassShooter["hp"]}\nATAQUE: {playerClassShooter["atk"]}\nDEFESA: {playerClassShooter["def"]}\nVELOCIDADE: {playerClassShooter["spd"]}\n')
        print(f'CLASSE: {playerClassMage["class"]}\nDESCRIÇÃO: \nATRIBUTOS:\nSAÚDE: {playerClassMage["hp"]}\nATAQUE: {playerClassMage["atk"]}\nDEFESA: {playerClassMage["def"]}\nVELOCIDADE: {playerClassMage["spd"]}\n')
        print(f'CLASSE: {playerClassDemon["class"]}\nDESCRIÇÃO: \nATRIBUTOS:\nSAÚDE: {playerClassDemon["hp"]}\nATAQUE: {playerClassDemon["atk"]}\nDEFESA: {playerClassDemon["def"]}\nVELOCIDADE: {playerClassDemon["spd"]}\n')
        
        playerInputChoose = input('> Digite o nome da classe escolhida: ')
        
        if (playerInputChoose.capitalize() == playerClassWarrior['class']):
            playerClass = playerClassWarrior
        if (playerInputChoose.capitalize() == playerClassShooter['class']):
            playerClass = playerClassShooter
        if (playerInputChoose.capitalize() == playerClassMage['class']):
            playerClass = playerClassMage
        if (playerInputChoose.capitalize() == playerClassDemon['class']):
            playerClass = playerClassDemon
        # Criar Personagem fim ---
