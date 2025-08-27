intake = input("Anna minulle numero: ")
smallest = 0
biggest = 0

while intake != "":
    numbers = float(intake)
    if smallest > numbers:
        smallest = numbers
    elif biggest < numbers:
        biggest = numbers
    intake = input("Anna minulle numero: ")

print(f"Suurin numero oli {biggest:.2f} ja pienin oli {smallest:.2f}.")