def ampelsteuerung(farbe):
    print(f"Die Ampel zeigt {farbe}!")
    farbe_klein = farbe.lower()
    if farbe_klein == "rot":
        print("Du musst stehen bleiben!")
    else:
        print("Du darfst fahren!")

ampelsteuerung("Rot")