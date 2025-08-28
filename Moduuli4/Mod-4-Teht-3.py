intake = input("Anna minulle numero: ")
smallest = 0
biggest = 0
no_numbers = False

if intake == "":
    print("Et antanut yhtään numeroa")
    no_numbers = True

while intake != "":
    numbers = float(intake)
    if smallest > numbers:
        smallest = numbers
    elif biggest < numbers:
        biggest = numbers
    intake = input("Anna minulle numero: ")

if no_numbers == False:
    print(f"Suurin numero oli {biggest:.2f} ja pienin oli {smallest:.2f}.")