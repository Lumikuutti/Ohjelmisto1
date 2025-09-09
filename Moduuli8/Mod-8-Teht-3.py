seasons = ("Kevät", "Kesä", "Syksy", "Talvi")
months = ("Tammi", "Helmi", "Maalis", "Huhti", "Touko", "Kesa", "Heina", "Elo", "Syys", "Loka", "Marras", "Joulu")
month = int( input("Anna kuukauden numero: "))

#kirjoitettu if lauseilla, koska koodaaja ei keksi miten kirjoittaa monikon monikkoa josta voi vielä käyttää arvoja jos se on edes mahdollista
if 0 < month < 3 or month == 12:
    print(f"{month}. kuukausi on {months[month-1]}kuu ja vuoden aika on {seasons[3]}")
elif 2 < month < 6:
    print(f"{month}. kuukausi on {months[month - 1]}kuu ja vuoden aika on {seasons[0]}")
elif 5 < month < 9:
    print(f"{month}. kuukausi on {months[month - 1]}kuu ja vuoden aika on {seasons[1]}")
elif 8 < month < 12:
    print(f"{month}. kuukausi on {months[month - 1]}kuu ja vuoden aika on {seasons[2]}")
else:
    print(f"{month} ei ole minkään kuukauden numero.")