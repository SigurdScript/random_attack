import random

class Character:
    def __init__(self, name, life):
        self.name = name
        self.life = life
        self.strength = random.randint(0,50)
    