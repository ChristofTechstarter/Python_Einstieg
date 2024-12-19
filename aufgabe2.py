# 1. Aktuelles Datum und Uhrzeit ausgeben:
# ○ Importiere das datetime-Modul.
# ○ Erstelle eine Funktion aktuelles_datum_und_uhrzeit(), die das
# aktuelle Datum und die aktuelle Uhrzeit im Format TT.MM.JJJJ HH:MM:SS
# ausgibt.
import datetime


def aktuelles_datum_und_uhrzeit():
    return datetime.datetime.now().strftime("%d.%m.%Y %X")


# print(aktuelles_datum_und_uhrzeit())

# 2. Differenz bis zum Jahresende berechnen:
# ○ Schreibe eine Funktion tage_bis_jahresende(), die die Anzahl der Tage
# vom aktuellen Datum bis zum 31. Dezember des aktuellen Jahres berechnet.
# ○ Hinweis: Verwende datetime.date oder datetime.datetime zur
# Berechnung.


def tage_bis_jahresende():
    heute = datetime.date.today()
    heute_jahr = heute.year
    jahresende = datetime.date(heute_jahr, 12, 31)

    return (jahresende - heute).days


# print(tage_bis_jahresende())

# 3. Benutzerdefiniertes Datum:
# ○ Implementiere eine Funktion tage_bis_datum(), die ein vom Benutzer
# eingegebenes Datum im Format TT.MM.JJJJ einliest und die Anzahl der
# Tage vom aktuellen Datum bis zu diesem Datum berechnet.
# ○ Tipp: Verwende input() für die Benutzereingabe und prüfe, ob das
# eingegebene Datum gültig ist. Falls nicht, soll der Benutzer eine neue Eingabe
# machen.


def tage_bis_datum():
    while True:
        try:
            eingabe_datum = input("Bitte ein Datum im Format TT.MM.JJJJ eingeben: ")
            ziel_datum = datetime.datetime.strptime(eingabe_datum, "%d.%m.%Y").date()
            datum_heute = datetime.date.today()
            tage = (ziel_datum - datum_heute).days

            if ziel_datum < datum_heute:
                print(
                    "Das Eingegebene Datum liegt in der Vergangenheit, bitte wähle ein Neues!"
                )
                continue

            print(f"Es sind noch {tage} Tage bis zum {ziel_datum.strftime('%d.%m.%Y')}")
            break
        except ValueError:
            print(
                "Das von dir eingegebene Datum ist ungültigt, bitte das Datum im Format TT.MM.JAHR angeben!"
            )


# tage_bis_datum()


# 4. Wochentag berechnen:
# ○ Erstelle eine Funktion wochentag_berechnen(), die den Wochentag für ein
# beliebiges eingegebenes Datum berechnet und ausgibt (z. B. Montag,
# Dienstag usw.).


def wochentag_berechnen():

    deutsche_wochentage = [
        "Montag",
        "Dienstag",
        "Mittwoch",
        "Donnerstag",
        "Freitag",
        "Samstag",
        "Sonntag",
    ]

    while True:
        try:

            eingabe = input("Bitte ein Datum im Format TT.MM.JJJJ eingeben: ")

            datum = datetime.datetime.strptime(eingabe, "%d.%m.%Y")

            wochentag_index = datum.weekday()

            wochentag = deutsche_wochentage[wochentag_index]

            print(
                f"Der Wochentag für das Datum {datum.strftime('%d.%m.%Y')} ist: {wochentag}"
            )
            break
        except ValueError:
            print("Ungültiges Datum! Bitte gib ein Datum im Format TT.MM.JJJJ ein.")


# wochentag_berechnen()

# 5. Zeitverschiebung berechnen:
# ○ Implementiere eine Funktion zeit_in_zukunft(), die eine Eingabe von
# Minuten, Stunden oder Tagen vom Benutzer entgegennimmt und das Datum
# und die Uhrzeit berechnet, die nach dieser Zeitspanne liegt.
# ○ Beispiel: Wenn der Benutzer 2 Stunden eingibt und die aktuelle Zeit 14:00
# ist, sollte das Programm 16:00 ausgeben.


def zeit_in_zukunft():
    while True:
        try:
            print(
                "Bitte geben Sie die Zeitspanne ein, die in die Zukunft verschoben werden soll:"
            )
            tage = int(input("Anzahl der Tage: "))
            stunden = int(input("Anzahl der Stunden: "))
            minuten = int(input("Anzahl der Minuten: "))

            aktuelle_zeit = datetime.datetime.now()

            zeitverschiebung = datetime.timedelta(
                days=tage, hours=stunden, minutes=minuten
            )
            zukunftszeit = aktuelle_zeit + zeitverschiebung

            print("Aktuelle Zeit:", aktuelle_zeit.strftime("%d-%m-%dY %H:%M:%S"))
            print("Zukünftige Zeit:", zukunftszeit.strftime("%d-%m-%Y %H:%M:%S"))
            break
        except ValueError:
            print("Ungültige Eingabe! Bitte gib eine Zahl ein!")


zeit_in_zukunft()
