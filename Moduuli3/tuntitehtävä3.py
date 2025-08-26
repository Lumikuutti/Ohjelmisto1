#kysytään matikan, fysiikan ja kemian tulokset
math_result = float( input("Ilmoita matematiikan tulos: "))
physics_result = float( input("Ilmoita fysiikan tulos: "))
chem_result = float( input("Ilmoita kemian tulos: "))

if math_result or physics_result or chem_result < 50:
    print("Et voi saada stipendiä, jokin tuloksistasi oli alle 50.")
elif math_result and physics_result >= 90 or chem_result >= 95:
    (print("Sait stipending, onneksi olkoon!"))
else:
    print("Et saanut ikävä kyllä stipendiä.")