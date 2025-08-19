import math

circle_r_str = input('Anna ympyrän säde: ')
circle_r = float(circle_r_str)

circle_area = math.pi * float(circle_r) ** 2
print(f'Ympyrän alue on: {circle_area:.2f}.')
