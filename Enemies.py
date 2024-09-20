import random

class Slime(): # Defines the enemy Slime
    def __init__(self):
        self.Enemy = "Slime"
        self.Shealth = random.randint(15,25)
        self.Sdodgechance = 2
        self.attack = random.randint(1,3)
slime = Slime()

def JumpAt(EnemyAttack, Enemy, PlayerDodgeChance, PlayerHealth): # Slime's Only Attack
    EnemiesUsedBy = ["Slime"] # Defines the enemies that can use this attack (just in case)
    if Enemy in EnemiesUsedBy: # Checks the enemy using this attack can use this attack
        Dodge = random.randint(1,100)
        if PlayerDodgeChance >= Dodge: # Checks if the player dodged
            print("You dodged the attack")
        else:
            Damage = random.randint(EnemyAttack - 1, EnemyAttack + 1)
            if Damage < 1:
                Damage = 1
                PlayerHealth = PlayerHealth - Damage # Deals the damage to the player
            else:
                PlayerHealth = PlayerHealth - Damage
    else:
        pass

