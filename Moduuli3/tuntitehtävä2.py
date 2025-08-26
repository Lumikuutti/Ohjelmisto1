used_hours = float( input("Anna kuinka monta kilowatti tuntia olet kuluttanut numerona: "))

if 0 > used_hours <= 50:
    laskutus = used_hours * 0.10
    print(f"Sähkölaskusi on {laskutus:.2f} euroa.")
elif 50 > used_hours <= 200:
    laskutus = 50 * 0.10 + (used_hours - 50) * 0.8
    print(f"Sähkölaskusi on {laskutus:.2f} euroa.")
elif used_hours > 200:
    laskutus = 50 * 0.10 + 150 * 0.8 + (used_hours - 200) * 0.6
    print(f"Sähkölaskusi on {laskutus:.2f} euroa.")
else:
    print("ERROR: Annettua arvoa ei voi käyttää.")