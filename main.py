'''
DUNGEON MAN 1.5 - 2024 ver
Author: Gustavo Mello
Description: RPG Experimental Backend Game
'''

import spawner as sp
import market
import interations as ui

# -- "funções" --

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