given_user = input("Anna käyttäjä tunnus: ")
given_pass = input("Anna salasana: ")
attempts = 1

while (given_user != "python" or given_pass != "rules") and not attempts >= 5:
    print("Joko käyttäjätunnus tai salasana on väärin.")
    attempts = attempts + 1
    given_user = input("Anna käyttäjä tunnus: ")
    given_pass = input("Anna salasana: ")

if attempts == 5:
    print("Pääsy evätty liian monen virheellisen yrityksen takia.")
else:
    print("Tervetuloa!")