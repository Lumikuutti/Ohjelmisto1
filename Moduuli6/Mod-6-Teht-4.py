numbers = [1, 4, 6, 8, 9, 3, 7, 2, 4]

#definataan funktio
def adding(list):
    added = 0
    for number in list:
        added =  number + added
    return added

added = adding(numbers)

print(added)