import random
amount_to_throw = int( input("Anna kuinka monta arpakuutiota heitetään: "))

if amount_to_throw < 0:
    print("En voi heittää negatiivista määrää arpakuutiota.")

else:
    thrown = 0
    added = 0
    rolled = []
    while thrown < amount_to_throw:
        rolled.append(random.randint(1,6))
        thrown = thrown + 1
for roll in rolled:
    added = added + roll

print(f"Heitettyjen arpakuutioden arvojen summa on: {added}")