import random
    

def actions(attacker,defender):
    print('1) Ataque devil: 1-10')
    print('2) Ataque medio: 11-20')
    print('3) Ataque fuerte: 21-50')
    
    try:
        value = int(input('Elige tu ataque: '))
        if value == 1:
            print(f'{attacker.name} LANZA ATAQUE DEVIL!')
            wound = random.randint(1,10)
            attack(defender, wound)
            info(defender)
            
        elif value == 2:
            print(f'{attacker.name} LANZA ATAQUE MEDIO!')
            wound = random.randint(11,20)
            attack(defender, wound)
            info(defender)
            
        elif value == 3:
            print(f'{attacker.name} LANZA ATAQUE FUERTE')
            wound = random.randint(21,50)
            attack(defender, wound)
            info(defender)
            
        else: 
            print('Accion invalida')
        
    except ValueError:
        print('ATENCIÓN: Debe ingresar un número entero.')
            
def attack(defender, wound):
    print(f'{defender.name} recive {wound} de daño')
    defender.life = defender.life - wound
    
def info(player):
    if player.life < 0:
        print(f'{player.name} ha Perdido!')
    else:
        print(f'{player.name} tiene {player.life} de vida restante \n')