def ampelsteuerung(farbe):
    print(f"Die Ampel zeigt {farbe}!")
    farbe_klein = farbe.lower()
    if farbe_klein == "rot":
        print("Du musst stehen bleiben!")
    else:
        print("Du darfst fahren!")

print("Welche Farbe zeigt die Ampel? (Rot, Gelb oder Grün)")
farbe = input()

ampelsteuerung(farbe)