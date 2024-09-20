import random

class Player():
    def __init__(self):
        self.health = 100
        self.attack = 3
        self.dodge_chance = 3


player = Player()

def Slash(Enemyhealth, EnemyDodgeChance, PlayerAttack):
    Miss = random.randint(1,100)
    if Miss <= 20:
        print("Your slash missed!")
    else:
        Dodge = random.randint(1,100)
        if Dodge >= EnemyDodgeChance:
            print("The enemy dodged")
        else:
            damage = random.randint(PlayerAttack - 1, PlayerAttack + 1)
            Enemyhealth = Enemyhealth - damage