import random
sides = int( input("Kuinka moni sivuista noppaa heitetään kunnes saadaan isoin noppa luku: "))

def diceroll():
    roll = random.randint(1, sides)
    return roll

print("Heitetään noppaa!")
roll = diceroll()
while roll < sides:
    print(f"{roll}, yritetään uudestaan.")
    roll = diceroll()
print(f"{roll}, jes, suurin noppa luku!")