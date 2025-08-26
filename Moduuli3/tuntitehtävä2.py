used_hours = float( input("Anna kuinka monta kilowatti tuntia olet kuluttanut numerona: "))

if used_hours <= 50:
    laskutus = used_hours * 10
    print(f"Sähkölaskusi on {laskutus:.2f} senttiä.")
elif 50 > used_hours < 200:
    laskutus = 50 * 10 + (used_hours - 50) * 8
    print(f"Sähkölaskusi on {laskutus:.2f} senttiä.")
elif 150 > used_hours:
    laskutus = 50 * 10 + 150 * 8 + (used_hours - 200) * 6
    print(f"Sähkölaskusi on {laskutus:.2f} senttiä.")
else:
    print("ERROR: Annettua arvoa ei voi käyttää.")