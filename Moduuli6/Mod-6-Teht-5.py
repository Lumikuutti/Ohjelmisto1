#definataan funktio
def two_divisible(selection):
    parilliset = []
    for number in selection:
        if number % 2 == 0:
            parilliset.append(number)
    return parilliset

numbers = [1, 4, 6, 8, 9, 5, 3, 7, 2, 4]
new_list = two_divisible(numbers)

print(numbers)
print(new_list)