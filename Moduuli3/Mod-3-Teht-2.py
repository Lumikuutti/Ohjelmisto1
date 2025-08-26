room_type = input("Ilmoita hyttiluokkasi (LUX, A, B, C): ")

if room_type == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif room_type == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif room_type == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif room_type == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")