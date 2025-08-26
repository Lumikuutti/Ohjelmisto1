year = int( input("Anna vuosi: "))

if (year % 4) == 0 and not (year % 100) == 0:
    print(f"Vuosi {year:.0f} on karkausvousi.")
elif (year % 100) == 0 and (year % 400) == 0:
    print(f"Vuosi {year:.0f} on karkausvuosi.")
else:
    print(f"Vuosi {year:.0f} ei ole karkausvuosi.")