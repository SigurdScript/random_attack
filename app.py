from character import Character
import random

name_player1 = input('Nombre de jugador 1: ')
name_player2 = input('Nombre de jugador 2: ')

player1 = Character(name_player1, 100)
player2 = Character(name_player2, 100)

fight = True
turn = 0

def attack(attacker,defender):
    print(f'Es el Turno de {attacker.name} \n')
    print(f'{attacker.name} Lanza ataque!')
    print(f'{defender.name} recive {attacker.strength} de daño')
    

    
def random_strength(player):
    player.strength = random.randint(0,50)
    
    
while fight:
    if player1.life > 0 and player2.life > 0:
        if turn == 0:
            attack(player1, player2)
            player2.life = player2.life - player1.strength
            random_strength(player1)
            if player2.life < 0:
                print(f'{player2.name} ha Perdido!')
            else:
                print(f'{player2.name} tiene {player2.life} de vida restante')
            turn = 1
            # break
            # fight = False
        else:
            attack(player2,player1)
            player1.life = player1.life - player2.strength
            random_strength(player2)
            if player1.life < 0:
                print(f'{player1.name} ha Perdido!')
            else:
                print(f'{player1.name} tiene {player1.life} de vida restante')
            turn = 0
    else:
        if player1.life <= 0:
            fight = False
            print(f'{name_player2} Gano el COMBATE!')
        else:
            fight = False
            print(f'{name_player1} Gano el COMBATE!')

