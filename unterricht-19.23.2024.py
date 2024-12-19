import datetime

# 3. Benutzerdefiniertes Datum:
# ○ Implementiere eine Funktion tage_bis_datum(), die ein vom Benutzer
# eingegebenes Datum im Format TT.MM.JJJJ einliest und die Anzahl der
# Tage vom aktuellen Datum bis zu diesem Datum berechnet.
# ○ Tipp: Verwende input() für die Benutzereingabe und prüfe, ob das
# eingegebene Datum gültig ist. Falls nicht, soll der Benutzer eine neue Eingabe
# machen.


def tage_bis_datum():
    date_input = input("Bitte ein Datum im Format TT.MM.JAHR eingeben:")
    date_input_convert = datetime.datetime.strptime(date_input, "%d.%m.%Y").date()
    date_today = datetime.date.today()
    days_diffrence = (date_input_convert - date_today).days
    return days_diffrence


# print(f"Es sind noch {tage_bis_datum()} Tage")


# 4. Wochentag berechnen:
# ○ Erstelle eine Funktion wochentag_berechnen(), die den Wochentag für ein
# beliebiges eingegebenes Datum berechnet und ausgibt (z. B. Montag,
# Dienstag usw.).


def wochentag_berechnen():
    weekdays_german = [
        "Montag",
        "Dienstag",
        "Mittwoch",
        "Donnerstag",
        "Freitag",
        "Samstag",
        "Sonntag",
    ]
    date_input = input("Bitte das Datum im Format TT.MM.JAHR eingeben: ")
    date_input_convert = datetime.datetime.strptime(date_input, "%d.%m.%Y")
    weekday_index = date_input_convert.weekday()
    weekday_german = weekdays_german[weekday_index]
    print(f"Der {date_input} ist ein {weekday_german}")


wochentag_berechnen()
