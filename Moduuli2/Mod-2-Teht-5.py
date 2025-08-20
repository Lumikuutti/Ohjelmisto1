leiviskat_str = input('Anna leiviskät: ')
leiviskat = float(leiviskat_str)
leiviskat_nauloina = leiviskat *20

naulat_str = input('Anna naulat: ')
naulat = float(naulat_str)
naulat_luoteina = (naulat + leiviskat_nauloina)*32

luodit_str = input('Anna luodit: ')
luodit = float(luodit_str)
yht_paino = (naulat_luoteina + luodit)*13.3

luodit_kg = yht_paino // 1000
luodit_g = yht_paino % 1000

print('Paino on nykyaikaisin mitoin:')
print(f'{luodit_kg:.0f} kilogrammaa ja {luodit_g:.0f} grammaa.')