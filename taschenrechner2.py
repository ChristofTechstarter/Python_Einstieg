import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


def potenz(x, y):
    return x**y


def sinus(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


def calculator():
    print("\nWillkommen bei Christof's Taschenrechner")
    print("Bitte wählen Sie eine der folgenden Optionen aus:")
    print("(1) Grundrechenfunktionen")
    print("(2) Winkelfunktionen")
    print("(3) Programm beenden")


def grundrechenarten():
    print("\nGrundrechenfunktionen")
    print("Bitte wählen Sie eine der folgenden Optionen aus:")
    print("(1) Addieren")
    print("(2) Subtrahieren")
    print("(3) Multiplizieren")
    print("(4) Dividieren")
    print("(5) Potenzen")
    print("(6) Zurück")


def winkelfunktionen():
    print("\nWinkelfunktionen")
    print("Bitte wählen Sie eine der folgenden Optionen aus:")
    print("(1) Sinusfunktion")
    print("(2) Kosinusfunktion")
    print("(3) Tangensfunktion")
    print("(4) Zurück")


while True:
    calculator()
    try:

        auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-3): "))

        if auswahl == 1:
            while True:
                grundrechenarten()
                try:

                    auswahl = int(
                        input("\nBitte wählen Sie Ihre Operation aus (1-6): ")
                    )

                    if auswahl in [1, 2, 3, 4, 5]:

                        zahl1 = float(input("Geben Sie die erste Zahl ein: "))
                        zahl2 = float(input("Geben Sie die zweite Zahl ein: "))

                        if auswahl == 1:
                            print(f"Das Ergebnis der Addition ist: {add(zahl1, zahl2)}")
                        elif auswahl == 2:
                            print(
                                f"Das Ergebnis der Subtraktion ist: {subtract(zahl1, zahl2)}"
                            )
                        elif auswahl == 3:
                            print(
                                f"Das Ergebnis der Multiplikation ist: {mult(zahl1, zahl2)}"
                            )
                        elif auswahl == 4:
                            if zahl2 != 0:
                                print(
                                    f"Das Ergebnis der Division ist: {div(zahl1, zahl2)}"
                                )
                            else:
                                print(f"Fehler: Division durch Null ist nicht erlaubt!")
                        elif auswahl == 5:
                            print(
                                f"Das Ergebnis der Potenz ist: {potenz(zahl1, zahl2)}"
                            )
                    elif auswahl == 6:
                        break
                    else:
                        print(
                            f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 6."
                        )

                except ValueError:
                    print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
        elif auswahl == 2:
            while True:
                winkelfunktionen()
                try:
                    auswahl = int(
                        input("\nBitte wählen Sie Ihre Operation aus (1-4): ")
                    )
                    if auswahl in [1, 2, 3]:

                        zahl1 = float(input("Geben Sie eine Zahl ein: "))

                        if auswahl == 1:
                            print(f"Das Ergebnis der Sinusfunktion ist: {sinus(zahl1)}")
                        elif auswahl == 2:
                            print(f"Das Ergebnis der Kosinusfunktion ist: {cos(zahl1)}")
                        elif auswahl == 3:
                            print(f"Das Ergebnis der Tangensfunktion ist: {tan(zahl1)}")
                    elif auswahl == 4:
                        break
                    else:
                        print(
                            f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 4."
                        )
                except ValueError:
                    print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
        elif auswahl == 3:
            print(f"Der Taschenrechner wird beendet. Auf Wiedersehen!")
            break
        else:
            print(f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 3.")

    except ValueError:
        print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
