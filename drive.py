print("Welche Farbe zeigt die Ampel? (Rot, Gelb oder Grün)")
farbe = input()
farbe_klein = farbe.lower()

if  farbe_klein == "rot":
    print("Du musst stehen bleiben!")
else:
    print("Du darfst fahren!")