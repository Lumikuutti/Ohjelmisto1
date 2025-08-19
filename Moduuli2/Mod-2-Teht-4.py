number1_str = input('Anna ensimmäinen numero: ')
number2_str = input('Anna toinen numero: ')
number3_str = input('Anna kolmas ja viimeinen numero: ')

number1 = float(number1_str)
number2 = float(number2_str)
number3 = float(number3_str)

numbersum = number1 + number2 + number3
numbertotal = number1 * number2 * number3
numberaverage = (number1 + number2 + number3)/3

print(f'Numeroiden summa on: {numbersum:.2f}')
print(f'Numeroiden tulo on: {numbertotal:.2f}')
print(f'Numeroiden keskiarvo on: {numberaverage:.2f}')