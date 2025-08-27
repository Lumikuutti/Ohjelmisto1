tuumat = float(input("Anna tuumien määrä: "))

while tuumat >= 0:
    print(f"{tuumat:.2f} tuumaa on {(tuumat * 2.54):.2f} senttimetriä.")
    tuumat = float(input("Anna tuumien määrä: "))

print("Kiitos convertterin käytöstä.")