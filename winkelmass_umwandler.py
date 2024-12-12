# Schreibe ein Programm, das zu einem gegebenen Winkel im Bogenmass
# (Eingabe in der Konsole durch den Benutzer), 
# den entsprechenden Winkel im Gradmass berechnet. 
# Die Ausgabe soll mit Grad (°), Bogenminuten (') 
# und Bogensekunden (") ausgegeben werden.

from math import pi

winkel_grad = float(input("Bitte gib deinen Winkel (in Gradmaß) an\n"))
winkel_bogen = (winkel_grad / 180) * pi

print(f"Dein Winkel {winkel_grad}° entspricht {winkel_bogen} in Bogenmaß")
