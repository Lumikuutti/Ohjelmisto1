import random
answer = random.randint(1, 10)
guess = int( input("Arvaa luku väliltä 1-10: "))

while answer != guess:
    if answer > guess:
        print (" Liian pieni arvaus. Yritä uudelleen!")
    else:
        print(" Liian suuri arvaus. Yritä uudelleen!")
    guess = int(input("Arvaa luku väliltä 1-10: "))

print ("Oikein! Onneksi olkoon!")