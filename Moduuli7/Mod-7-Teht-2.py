names = set()
name = input("Anna nimi tai lopeta painamalla Enter: ")
if name == "":
    print("Et antanut yhtään nimeä.")
else:
    while name != "":
        if name in names:
            print("Aiemmin syötetty nimi.")
            name = input("Anna nimi tai lopeta painamalla Enter: ")
        else:
            print("Uusi nimi.")
            names.add(name)
            name = input("Anna nimi tai lopeta painamalla Enter: ")
    print(f"Kaikki syöttämäsi nimet mielivaltaisessa järjesteksyssä, kerran per nimi: {names}")