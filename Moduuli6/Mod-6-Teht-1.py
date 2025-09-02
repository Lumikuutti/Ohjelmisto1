import random

def diceroll():
    return random.randint(1, 6)

print("Heitetään noppaa!")
roll = diceroll()
while roll < 6:
    print(f"{roll}, yritetään uudestaan.")
    roll = diceroll()
print(f"{roll}, jes, kuutonen!")