fish_length = float( input("Anna kuhan pituus senttimetreinä: "))

if fish_length < 37:
    too_small_by = 37 - fish_length
    print(f"Vapauta kuha takaisin järveen, se on liian pieni {too_small_by:.2f} senttimetrillä.")
else:
    print("Nauti hyvin pyydetystä kuhastasi!")