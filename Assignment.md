# Aufgaben für den Nachmittag: Python-Code in Arbeitsschritte beschreiben

**Abgabe**: Text ()

## Aufgabe 1: Einfache Entscheidungen mit `if`-Statements (25 Punkte)

**Ziel:** Verstehen, wie Entscheidungen im Code in Arbeitsschritte übersetzt werden können.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 10:
    print("Die Zahl ist größer als 10.")
else:
    print("Die Zahl ist 10 oder kleiner.")
```

- Schreibe die Arbeitsschritte auf.

### Anwort:
- Zeile 12: die Variable `zahl` fordert einen user Input mit `input()` an, um Mathematische Operationen durchzuführen wird das `String` Ergebnis des Sser Inputs mithilfe von `int()` in eine Zahl konvertiert.
- Zeile 13: Eine `if` Bedingung die überprüft ob meine Variable `zahl` größer als 10 ist
- Zeile 14: was passieren soll wenn die Bedingung in zeile 13 `True` ist, in diesem Fall ein `print()` Befehl, der in `Stringform` "Die Zahl ist größer als 10." auf der Konsole ausgegeben wird
- Zeile 15: `else` bezieht sich auf das `if` von Zeile 13 und erläutert was passieren soll wenn `if` von Zeile 13 `False` ist
- Zeile 16: mit dem `print()` Befehl, wird der `String` "Die Zahl ist 10 oder kleiner." in der Konsole ausgegeben

---

## Aufgabe 2: Listen verstehen und mit Python erstellen (20 Punkte)

**Ziel:** Verstehen, wie Datenstrukturen wie Listen verwendet werden können.

Code-Beispiel:

```python
zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])
```

- Schreibe die Arbeitsschritte auf.

### Antwort:
- Zeile 37: Die Variable `zahlen` beinhatet eine Liste, diese ist zu erkennen an den `[]` und einträge werden mit einem `,` getrennt, in diesem Beispiel befinden sich die Zahlen 1 - 5 in der Liste
- Zeile 38: Mit dem `print` befehl wird über die Konsole ausgegeben "Die erste Zahl ist: 1", mit `zahlen[0]` soll Python in unsere Liste `zahlen` schauen und den `Index 0` anzeigen, da Listen immer von 0 beginnen, würde in unserem Beispiel die 1 ausgegeben werden 
- Zeile 39: Mit dem `print` befehl wird über die Konsole ausgegeben "Die letzte Zahl ist: 5", mit `zahlen[-1]` soll Python in unsere Liste `zahlen` schauen und den `Index -1`, also den Letzten Eintrag bzw. den Ersten von hinten, ausgeben

**Zusatzaufgabe:** Erstelle selbst eine Liste mit Wochentagen und schreibe die Arbeitsschritte auf.
```python
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag" , "Sonntag"]
print("Der 4. Wochentag lautet: ", wochentage[3])
```
- Zeile 51: Variable `wochentage` als Liste mit allen Wochentagen im Format `String`
- Zeile 52: Mit `print()` wird "Der 4. Wochentag lautet: Donnerstag" ausgegeben, da wir uns mit `wochentage` auf unsere Liste beziehen und dort soll der index `3`, in unserem Fall Donnerstag, ausgegeben werden
---

## Aufgabe 3: Entscheidungslogik erweitern (25 Punkte)

**Ziel:** Die Funktionsweise von mehreren Bedingungen in Python verstehen und in Arbeitsschritte übertragen.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")
```

- Schreibe die Arbeitsschritte auf.

### Antwort:
- Zeile 65: Die Variable `zahl` fodert mit `input` eine Eingabe des Users im Format `String` und mit `int()` wird die Eingabe in ein integer konvertiert, damit wir Mathematische Operationen durchführen können
- Zeile 66: Eine `if` Bedingung die besagt: unsere Variable `zahl` ist größer als 0
- Zeile 67: sollte die `if` Bedingung von Zeile 66 `True` sein, wird mit dem `print()` Befehl der `String` "Die Zahl ist positiv" auf der Konsole ausgegeben
Zeile 68: Eine `elif (else if)` Bedingung, diese wird erst überprüft sofern die vorherige `if` bedingung `false` war, im Beisiel wird überprüft, ob `zahl` kleiner als 0 ist
- Zeile 69: Sollte die `elif` Bedingung aus Zeile 68 `True` sein, wird mit dem befehl `print()` der `String` "Die Zahl ist negativ" auf der Konsole ausgegeben
- Zeile 70: Eine `else` Bedingung wird ausgeführt sobald keine der vorherigen `if` und `elif` bedingungen `True` waren
- Zeile 71: mit dem `print()` Befehl wird ein String "Die Zahl ist null." auf der Konsole ausgegeben
---

## Aufgabe 4: Funktionen verstehen (20 Punkte)

**Ziel:** Lernen, wie Funktionen in Python definiert werden und was in jedem Arbeitsschritt passiert.

Code-Beispiel:

```python
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

zahl = int(input("Gib eine Zahl ein: "))
if ist_gerade(zahl):
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
```

- Schreibe die Arbeitsschritte auf.

### Antwort:
- Zeile 93: Mit `def`leiten wir eine neue Funktionsdefinition ein, danach folgt der Funktionsname in diesem Beispiel `ist_gerade` in den `()` weisen wir nun unsere `Argumente`, die nur für unsere Funktionsdefintion, auch `Scope` genannt, zu. In dem beispiel wäre es `zahl`
- Zeile 94: Eine `if` Bedingung die überprüft, ob das argument `zahl` durch 2 teilbar ist und einen Rest von 0 enthält
- Zeile 95: Sollte die `if` Bedingung aus Zeile 94 `True` sein, geben wir mit `return` den `boolean True` zurück
- Zeile 96: `else` wird nur ausgeführt wenn die vorherige `if` bedingung `False` war
- Zeile 97: gibt mit den `return` befehl, den `boolean False` zurück

- Zeile 99: die Variable `zahl` fordert mit `input()` einen `String` vom User und wandelt es mit `int()` in ein `integer` Datentyp
- Zeile 100: Eine `if` bedingung  mit unserer vorher definierten Funktion `ist_gerade`, hier würde python dann in Zeile 93 - 97 "nachschauen" was unsere funktion genau macht, aber diesmal würde er das Argument "zahl" aus der Funktionsdefinition, mit dem Argument von der Funktionsausführung austauschen, da diese in diesem fall gleich sind muss nichts "getauscht" werden
- Zeile 101: Falls unsere Funktion den Wert `true` zurück gibt, wird mit den `print()` befehl der String "Die Zahl ist gerade" auf der Konsole angezeigt.
- Zeile 102: `else` wird ausgeführt sobald alle vorherigen Bedingungen `False` waren
- Zeile 103: Falls unsere Funktion den Wert `False` zurück gibt, wird mit `print()` der `String` "Die Zahl ist ungerade" auf der Konsole ausgegeben
---

## Aufgabe 5: Benutzerinteraktion (10 Punkte)

**Ziel:** Die Struktur eines Programms mit Benutzereingaben und Ausgaben analysieren.

Code-Beispiel:

```python
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")
```

- Schreibe die Arbeitsschritte auf.

### Antwort:
- Zeile 129: die Variable `name` fordert mit `input()` einen `String` vom User
- Zeile 130: die Variable `alter` fordert mit `input()` einen `String` vom User und konvertiert diesen mit `int()` in einen `integer` datentyp
- Zeile 131: Mit `print(f"")` kann ein `formatierter String` angegeben werden, dies ermöglicht uns das direkte einbinden von Variablen, was mit den geschweiften klammern `{}` möglich ist, außerdem können wir auch z. B. Mathematische Operationen direkt in den String vornehmen wie z.B. `{alter + 10}` in dem direkt auf die variable `alter` 10 addiert werden und es wird dann auf der Konsole ausgegeben
---

Diese Aufgaben sind auf den bisherigen Stand der Vorlesung abgestimmt und bieten eine gute Balance zwischen Verständnis und Anwendung. Punkte sind proportional zur Komplexität der Aufgabe verteilt.