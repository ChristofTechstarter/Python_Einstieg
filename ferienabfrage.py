# Ferien:

# Winterferien 2025
# 24.12.2025 - 01.01.2026
# • 4 Urlaubstage
# • Letzter Unterrichtstag: 23.12.2024
# • Erster Unterrichtstag nach den Ferien ist der 02.01.2025

# Feiertage:
# Tag der deutschen Einheit
# 03.10.2024
# Reformationstag
# 31.10.2024
# 1. Weihnachtstag
# 25.12.2024
# 2. Weihnachtstag
# 26.12.2024
# Neujahr
# 01.01.2025
# Karfreitag
# 18.04.2025
# Ostermontag
# 21.04.2025
# Tag der Arbeit
# 01.05.2025
# Christi Himmelfahrt
# 29.05.2025
# Pfingstmontag
# 09.06.2025
# Tag der deutschen Einheit
# 03.10.2025
# Reformationstag
# 31.10.2025
# 1. Weihnachtstag
# 25.12.2025
# 2. Weihnachtstag
# 26.12.2025
# Neujahr
# 01.01.2026

feiertage = ["2024.10.03", "2024.10.31"]
feiertage2 = feiertage

datum = input("Bitte gib ein Datum ein (JAHR.MM.TT): ")

if datum >= "2024.12.24" and datum <= "2025.01.01":
    # Winterferien 2024
    print(
        f"An dem {datum} hast du Winterferien, der Unterricht beginnt wieder am: 2025.01.02"
    )
# Osterferien 2025
elif datum >= "2025.04.18" and datum <= "2025.04.21":
    print(
        f"An dem {datum} hast du Osterferien, der Unterricht beginnt wieder am: 2025.04.22"
    )
# Sommerferien 2025
elif datum >= "2025.08.11" and datum <= "2025.08.19":
    print(
        f"An dem {datum} hast du Sommerferien, der Unterricht beginnt wieder am: 2025.08.20"
    )
# Winterferien 2025
elif datum >= "2025.12.24" and datum <= "2026.01.01":
    print(
        f"An dem {datum} hast du Winterferien, der Unterricht beginnt wieder am: 2026.01.02"
    )
# Feiertage
elif datum == feiertage:
    print(f"An dem {datum} hast du keinen Unterricht, es ist ein Feiertag")
else:
    print(f"An dem {datum} hast du Unterricht!")
