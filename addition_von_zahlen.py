# Schreibe ein Programm, das den Benutzer nach zwei Zahlen fragt und deren Summe
# berechnet.

while True:
    try:

        zahl1 = input("Bitte nenne mir deine 1. Zahl:\n")
        zahl1_int = int(zahl1)
        zahl2 = input("Bitte nenne mir deine 2. Zahl:\n")
        zahl2_int = int(zahl2)
        break
    except ValueError:
        print("Bitte eine Zahl eingeben!")

print(f"Die Summe deiner genannten Zahlen ergibt: {zahl1_int + zahl2_int}")