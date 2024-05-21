'''
DUNGEON MAN 1.5 - 2024 ver
Author: Gustavo Mello
Description: RPG Experimental Backend Game
'''

import spawner as sp
import market
import interations as ui

# -- "funções" --

# Criar Personagem: ---
def createCharacter():
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
        return playerClassWarrior
    if (playerInputChoose.capitalize() == playerClassShooter['class']):
        return playerClassShooter
    if (playerInputChoose.capitalize() == playerClassMage['class']):
        return playerClassMage
    if (playerInputChoose.capitalize() == playerClassDemon['class']):
        return playerClassDemon
# Criar Personagem fim ---

# -- "funções" --


#Saudações // Menu Principal
print('### Bem-vindo a Dungeon Man ###')
print('--- ver 1.5 - mai 2024 ---')
start = input('Deseja iniciar o jogo? (S/N): ')
if (start.upper() == "N" or start == "NÃO"):
    exit()
else:
    playerName = input('> Digite um nome para seu personagem: ')
    print(f'\n>> Parabens! você criou: {playerName}, mas é preciso definir qual classe ele(a) pertence.')
    player = createCharacter()
    print(f"Isso! {playerName} é da classe {player['class']}!")


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