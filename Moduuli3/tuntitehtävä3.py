#kysytään matikan, fysiikan ja kemian tulokset
math_result = int( input("Ilmoita matematiikan tulos: "))
physics_result = int( input("Ilmoita fysiikan tulos: "))
chem_result = int( input("Ilmoita kemian tulos: "))

if (math_result or physics_result or chem_result) < 50:
    print("Et voi saada stipendiä, jokin tuloksistasi oli alle 50.")
elif (math_result and physics_result) > 90 or chem_result > 95:
    (print("Sait stipendin, onneksi olkoon!"))
else:
    print("Et saanut ikävä kyllä stipendiä.")