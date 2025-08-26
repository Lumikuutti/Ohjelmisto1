gender = input("Ilmoita sukupuolesi (AFAB tai AMAB): ")
hemo_glob = float( input("Ilmoita hemoglobiiniarvosi (g/l): "))

if gender == "AFAB":
    if hemo_glob < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo_glob < 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
elif gender == "AMAB":
    if hemo_glob < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo_glob < 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Jotain meni vikaan prosessissa.")