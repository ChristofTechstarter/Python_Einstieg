def ampelsteuerung(farbe):
    print(f"Die Ampel zeigt {farbe}")
    if farbe == "rot":
        print("Du musst stehen bleiben!")
    else:
        print("Du darfst fahren")

ampelsteuerung("rot")