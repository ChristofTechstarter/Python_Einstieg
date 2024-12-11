# Aufgabe: Wörterzähler
# Schreibe ein Python-Programm, das:

# - Den Benutzer nach einem Satz fragt.
# - Die Anzahl der Wörter in diesem Satz zählt.
# - Die Anzahl der Buchstaben (ohne Leerzeichen) in diesem Satz zählt.
# - Beides in einer verständlichen Ausgabe anzeigt.

print("Bitte gib hier einen Satz ein")
satz = input()

anzahl_woerter = len(satz.split())

anzahl_buchstaben = len(satz.replace(" ", ""))

print(f"Anzahl der Wörter: {anzahl_woerter}")
print(f"Anzahl der Buchstaben (ohne Leerzeichen): {anzahl_buchstaben}")