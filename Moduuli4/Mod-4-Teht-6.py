import random

total_points = 0
points_in_circle = 0

points_to_generate = int( input("Anna kuinka monta pistettä kokeillaan: "))

while total_points < points_to_generate:
    x = random.uniform (-1,1)
    y = random.uniform (-1, 1)
    total_points = total_points + 1
    if (x ** 2 + y ** 2) < 1:
        points_in_circle = points_in_circle +1

if points_to_generate <= 0:
    print("En voi laskea piin likimäärää negativiisesta määrästä lähtien tai ilman pisteitä ollenkaan.")

else:
    pii = (4 * points_in_circle) / total_points
    print (f"Piin likimääräinen arvo Monte Carlo methodilla on {pii:.4f}, {points_to_generate} genoroidun pisteen perusteella.")