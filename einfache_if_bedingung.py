# Schreibe ein Programm, das eine Zahl vom Benutzer einliest und überprüft, ob sie positiv,
# negativ oder null ist.

zahl = int(input("Bitte nenne mir eine Zahl: \n"))

if zahl < 0:
    print("Das ist eine negative Zahl!")

if zahl > 0:
    print("Das ist eine Positive Zahl!")

if zahl == 0:
    print("Deine Zahl ist 0!")