# Schreibe zunächst 4 Funktionen: add(x,y), subtract(x,y), mult(x,y) und
# div(x,y)
# potenzen,
# sinus/cos,
# temperaturumrechner von celsius in fahrenheit und umgekehrt,
#
# Jede dieser 4 Funktionen soll 2 Argumente annehmen: x und y, und die
# miteinander addieren, subtrahieren, multiplizieren oder dividieren
#
# Dann schreibt eine Funktion calculator(), die:
#
# Den User fragt, ob er addieren, subtrahieren, multiplizieren oder
# dividieren will
#
# Den user nach 2 Zahlen fragt
#
# Die entsprechende Funktion aufruft
#
# Das Ergebnis auf der Konsole anzeigt

# Import math Library
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
    return math.cos(x)


def calculator():
    print("\nWillkommen bei Christof's Taschenrechner")
    print("Bitte wählen Sie eine der folgenden Optionen aus:")
    print("(1) Addieren")
    print("(2) Subtrahieren")
    print("(3) Multiplizieren")
    print("(4) Dividieren")
    print("(5) Potenzen")
    print("(6) Sinusfunktion")
    print("(7) Cosinusfunktion")
    print("(8) Programm beenden")


while True:
    calculator()
    try:

        auswahl = int(input("\nBitte wählen Sie Ihre Operation aus (1-8): "))

        if auswahl in [1, 2, 3, 4, 5]:

            zahl1 = float(input("Geben Sie die erste Zahl ein: "))
            zahl2 = float(input("Geben Sie die zweite Zahl ein: "))

            if auswahl == 1:
                print(f"Das Ergebnis der Addition ist: {add(zahl1, zahl2)}")
            elif auswahl == 2:
                print(f"Das Ergebnis der Subtraktion ist: {subtract(zahl1, zahl2)}")
            elif auswahl == 3:
                print(f"Das Ergebnis der Multiplikation ist: {mult(zahl1, zahl2)}")
            elif auswahl == 4:
                if zahl2 != 0:
                    print(f"Das Ergebnis der Division ist: {div(zahl1, zahl2)}")
                else:
                    print(f"Fehler: Division durch Null ist nicht erlaubt!")
            elif auswahl == 5:
                print(f"Das Ergebnis der Potenz ist: {potenz(zahl1, zahl2)}")
        if auswahl in [6, 7]:
            zahl1 = float(input("Geben Sie die eine Zahl ein: "))
            if auswahl == 6:
                print(f"Das Ergebnis der Sinusfunktion ist: {sinus(zahl1)}")
            elif auswahl == 7:
                print(f"Das Ergebnis der Cosinusfunktion ist: {cos(zahl1)}")
        elif auswahl == 8:
            print(f"Der Taschenrechner wird beendet. Auf Wiedersehen!")
            break
        else:
            print(f"Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 5.")

    except ValueError:
        print(f"Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
