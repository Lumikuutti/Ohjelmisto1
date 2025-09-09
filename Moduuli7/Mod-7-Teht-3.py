airports = {"LATI":"Tirana International Airport",
            "EFHK":"Helsinki-Vantaan lentoasema"}

print("Valitse haluatko lisätä lentokentän, hakea lentokenttiä vai lopettaa.\n"
      "Lisääminen tapahtuu komennolla: add\n"
      "Haku tapahtuu komennolla: search\n"
      "Lopeta painamalla Enter.")
command = input("Mitä haluaisit tehdä: ")
while command != "":
    if command == "add":
        icao = input("Anna lentokentän ICAO koodi: ")
        name = input("Anna lentokentän nimi: ")
        airports[icao] = name
    elif command == "search":
        icao = input("Anna lentokentän ICAO koodi: ")
        if icao in airports:
            print(f"Lentokenttä löydetty, sen nimi on {airports[icao]}")
        else:
            print("Valitettavasti lentokenttää ei löydy tästä tietokannasta.")
    else:
        print("Virheellinen kommento.")
    command = input("Mitä haluaisit tehdä seuraavaksi: ")

print("Kiitos ohjelman käytöstä, näkemiin!")