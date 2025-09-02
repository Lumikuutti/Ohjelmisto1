import math

def euro_per_area(euros, diameter):
    area = math.pi * ((diameter/2) ** 2)
    #muutetaan neliösenttimetrit neliömetreiksi
    size = area * 10000
    unit_price = euros / size
    return unit_price

pizza1 = float( input("Anna pizzan numero 1 halkaisija senttimetreinä: "))
prize1 = float( input("Anna pizzan numero 1 hinta euroina: "))
pizza2 = float( input("Anna pizzan numero 2 halkaisija senttimetreinä: "))
prize2 = float( input("Anna pizzan numero 2 hinta euroina: "))

unit_price1 = euro_per_area(prize1, pizza1)
unit_price2 = euro_per_area(prize2, pizza2)

if unit_price1 > unit_price2:
    print(f"Pizza numero kaksi on yksikköhinnaltaan edullisempi, sen yksikköhinta on {unit_price2:.9f} euroa per neliömetri pizzaa.")
elif unit_price2 > unit_price1:
    print(f"Pizza numero yksi on yksikköhinnaltaan edullisempi, sen yksikköhinta on {unit_price1:.9f} euroa per neliömetri pizzaa.")
else:
    print("Pizzojen yksikköhinnat ovat samat!")