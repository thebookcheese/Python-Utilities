import random

class Player():
    def __init__(self):
        self.health = 100
        self.attack = 3
        self.dodge_chance = 3


player = Player()

def Slash(Enemyhealth, EnemyDodgeChance, PlayerAttack):
    Miss = random.randint(1,100)
    if Miss > 20:
        print("Your slash missed!")
    else:
        Dodge = random.randint(1,100)
        print(Dodge, "<", EnemyDodgeChance)
        if Dodge > EnemyDodgeChance:
            Damage = random.randint(PlayerAttack - 1, PlayerAttack + 1)
            Enemyhealth = Enemyhealth - Damage
            print("You dealt ",Damage," damage to the enemy. The enemy is on ",Enemyhealth)
        else:
            damage = random.randint(PlayerAttack - 1, PlayerAttack + 1)
            Enemyhealth = Enemyhealth - damage


def Chop(Enemyhealth, EnemyDodgeChance, PlayerAttack):
    Miss = random.randint(1,100)
    if Miss < 40:
        print("Your chop missed")
    else:
        Dodge = random.randint(1,100)
        if (Dodge - 10) <= EnemyDodgeChance:
            Damage = random.randint(PlayerAttack + 2, PlayerAttack + 5)
            Enemyhealth = Enemyhealth - Damage
            print("You dealt ",Damage," damage to the enemy. The enemy is on ",Enemyhealth)