def liters(x):
    conversion = x * 3.785
    return conversion

gallons = float( input("Anna bensiinin määrä nestegallonoina niin muutan ne litroiksi: "))
while gallons >= 0:
    print(f"Tuo määrä litroina on {liters(gallons)} litraa.")
    gallons = float(input("Anna bensiinin määrä nestegallonoina niin muutan ne litroiksi: "))

print("Kiitos konvertterin käytöstä.")