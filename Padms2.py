import random
import Player
import Enemies

def underline(text): # For underlining
    print("\u0332".join(text))

def Town():
    print("Do you want to go to the slime swamp?")
    SlimeSwamp()

def SlimeSwamp():
    print("You are going to the ")
    underline("slime swamp")
    print("You encounter a Slime with",Enemies.slime.Shealth,"health")
    SlimeHealth = Enemies.slime.Shealth
    SlimeDodgeChance = Enemies.slime.Sdodgechance
    while SlimeHealth > 0 and Player.player.health > 0:
        print("You encounter a Slime with",Enemies.slime.Shealth,"health")
        Attack = input("What attack do you want to use: \n Slash \n Chop \n").lower()
        if Attack == "slash":
            Player.Slash(SlimeHealth, SlimeDodgeChance, Player.player.health)
        elif Attack == "chop":
            Player.Chop(Enemies.slime.Shealth, Enemies.slime.Sdodgechance, Player.player.attack)
        else:
            print("Not valid attack")

Town()