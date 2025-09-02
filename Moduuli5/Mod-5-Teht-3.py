new_number = input("Anna luku tai paina Enter ohjelman lopettamiseksi: ")
numbers = []

while new_number != "":
    number = (int(new_number))
    numbers.append(number)
    for begin in range(1,(number+1)):
