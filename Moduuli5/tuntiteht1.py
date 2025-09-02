luvut = []
ei_lukuja = False
annettu_luku = int(input("Anna positiivine luku tai negatiivinen luku päättääksesi ohjelman: "))

if annettu_luku < 0:
    print("Et antanut yhtään lukua listaan.")
    ei_lukuja = True
while annettu_luku > 0:
    luvut.append (annettu_luku)
    annettu_luku = int(input("Anna positiivine luku tai negatiivinen luku päättääksesi ohjelman: "))

luvut.sort()
if not ei_lukuja:
    print(luvut)
if 10 in luvut:
    print("Luku 10 löytyi")
else:
    print("Lukua 10 ei löytynyt.")