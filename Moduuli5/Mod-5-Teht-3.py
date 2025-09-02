new_number = input("Anna luku tai paina Enter ohjelman lopettamiseksi: ")
alkuluku = False
if new_number == "":
    print("Lopetit ohjelman heti.")
else:
    #muutetaan annettu luku integraaliksi
    new_number = int(new_number)
    #käydään läpi onko luku jaollinen muilla kuin itsellään
    for x in range(2, new_number):
        if new_number % x == 0:
            alkuluku = False
            print("Luku ei ole alkuluku.")
            break
        else:
            alkuluku = True

    if alkuluku:
        print("Luku on alkuluku.")