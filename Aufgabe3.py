# Aufgabe: Palindrom-Überprüfung
# Schreibe ein Python-Programm, das:

# Den Benutzer nach einem Wort fragt.
# Überprüft, ob das Wort ein Palindrom ist (ein Wort, das von vorne und hinten gleich ist, z. B. "Otto" oder "Reittier").
# Eine Nachricht ausgibt, die dem Benutzer mitteilt, ob das Wort ein Palindrom ist oder nicht.
# Hinweis: Achte darauf, dass die Groß- und Kleinschreibung keine Rolle spielt.

print("Gib ein Wort ein")
wort = input()
wort_klein = wort.lower()

if wort_klein == wort_klein[::-1]:
    print("Das Wort ist ein Palindrom.")
else:
    print("Das Wort ist kein Palindrom.")