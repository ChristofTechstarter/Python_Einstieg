# Aufgabe: Summe und Durchschnitt berechnen
# Schreibe ein Python-Programm, das den Benutzer nach fünf Zahlen fragt, die der Benutzer eingibt. Dein Programm soll dann:

# Die Summe dieser fünf Zahlen berechnen.
# Den Durchschnitt dieser fünf Zahlen berechnen.
# Die Ergebnisse in einer verständlichen Ausgabe anzeigen.

print("Gib deine erste Zahl ein")
zahl1 = float(input())
print("Gib deine zweite Zahl ein")
zahl2 = float(input())
print("Gib deine dritte Zahl ein")
zahl3 = float(input())
print("Gib deine vierte Zahl ein")
zahl4 = float(input())
print("Gib deine fünfte Zahl ein")
zahl5 = float(input())

zahlen = [zahl1, zahl2, zahl3, zahl4, zahl5]

print("Die Summe deiner Zahlen beträgt: ", sum(zahlen))
print("Der Durchschnitt deiner Zahlen beträgt: ", sum(zahlen) / len(zahlen))