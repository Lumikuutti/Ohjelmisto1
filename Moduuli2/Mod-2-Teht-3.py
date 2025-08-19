side_a_str = input('Anna suorakulmion korkeus: ')
side_a = float(side_a_str)

side_b_str = input('Anna suorakulmion leveys: ')
side_b = float(side_b_str)

rectangle_area = side_b * side_a
rectangle_circ = 2*(side_b + side_a)

print(f'Suorakulmion piiri on: {rectangle_circ:.2f}')
print(f'Suorakulmion alue on: {rectangle_area:.2f}')
