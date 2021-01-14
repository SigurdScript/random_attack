import random

def attack(attacker,defender):
    print(f'Es el Turno de {attacker.name} \n')
    print(f'{attacker.name} Lanza ataque!')
    print(f'{defender.name} recive {attacker.strength} de daño')
    

def random_strength(player):
    player.strength = random.randint(0,50)
    
def info(player):
    if player.life < 0:
        print(f'{player.name} ha Perdido!')
    else:
        print(f'{player.name} tiene {player.life} de vida restante')