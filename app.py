from character import Character
from functions import attack,random_strength,info
import random

name_player1 = input('Nombre de jugador 1: ')
name_player2 = input('Nombre de jugador 2: ')

player1 = Character(name_player1, 100)
player2 = Character(name_player2, 100)

fight = True
turn = 0
    
while fight:
    if player1.life > 0 and player2.life > 0:
        if turn == 0:
            attack(player1, player2)
            player2.life = player2.life - player1.strength
            random_strength(player1)
            info(player2)
            turn = 1
            # break
            # fight = False
            
        else:
            attack(player2,player1)
            player1.life = player1.life - player2.strength
            random_strength(player2)
            info(player1)
            turn = 0
    else:
        if player1.life <= 0:
            fight = False
            print(f'{name_player2} Gano el COMBATE!')
        else:
            fight = False
            print(f'{name_player1} Gano el COMBATE!')

