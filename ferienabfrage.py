feiertage = [
    "2024.10.03",
    "2024.10.31",
    "2024.12.25",
    "2024.12.26",
    "2025.01.01",
    "2025.04.18",
    "2025.04.21",
    "2025.05.01",
    "2025.05.29",
    "2025.06.09",
    "2025.10.03",
    "2025.10.31",
    "2025.12.25",
    "2025.12.26",
    "2026.01.01",
]

datum = input("Bitte gib ein Datum ein (JAHR.MM.TT): ")


def feiertag(datum):
    if datum in feiertage:
        print(f"An dem {datum} hast du keinen Unterricht, es ist ein Feiertag")


# Winterferien 2024
if datum >= "2024.12.24" and datum <= "2025.01.01":
    feiertag(datum)
    print(
        f"An dem {datum} hast du Winterferien, der Unterricht beginnt wieder am: 2025.01.02"
    )
# Osterferien 2025
elif datum >= "2025.04.18" and datum <= "2025.04.21":
    feiertag(datum)
    print(
        f"An dem {datum} hast du Osterferien, der Unterricht beginnt wieder am: 2025.04.22"
    )
# Sommerferien 2025
elif datum >= "2025.08.11" and datum <= "2025.08.19":
    feiertag(datum)
    print(
        f"An dem {datum} hast du Sommerferien, der Unterricht beginnt wieder am: 2025.08.20"
    )
# Winterferien 2025
elif datum >= "2025.12.24" and datum <= "2026.01.01":
    feiertag(datum)
    print(
        f"An dem {datum} hast du Winterferien, der Unterricht beginnt wieder am: 2026.01.02"
    )
# Feiertage
elif datum in feiertage:
    print(f"An dem {datum} hast du keinen Unterricht, es ist ein Feiertag")
else:
    print(f"An dem {datum} hast du Unterricht!")
