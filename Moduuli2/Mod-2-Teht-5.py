leiviskat_str = input('Anna leiviskät: ')
leiviskat = float(leiviskat_str)
leiviskat_nauloina = leiviskat *20

naulat_str = input('Anna naulat: ')
naulat = float(naulat_str)
naulat_luoteina = (naulat + leiviskat_nauloina)*32

luodit_str = input('Anna luodit: ')
luodit = float(luodit_str)
luodit_grammoina = (naulat_luoteina + luodit)*13.3

print(f'Paino grammoina: {luodit_grammoina:.2f}')