#definataan funktio
def two_divisible(selection):
    for number in selection:
        if number % 2 != 0:
            selection.remove(number)
    return selection

numbers = [1, 4, 6, 8, 9, 3, 7, 2, 4]
new_list = two_divisible(numbers)

print(numbers)
print(new_list)