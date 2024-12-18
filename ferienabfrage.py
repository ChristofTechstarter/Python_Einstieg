import datetime


feiertage = [
    datetime.datetime(2024, 10, 3),
    datetime.datetime(2024, 10, 31),
    datetime.datetime(2024, 12, 25),
    datetime.datetime(2024, 12, 26),
    datetime.datetime(2025, 1, 1),
    datetime.datetime(2025, 4, 18),
    datetime.datetime(2025, 4, 21),
    datetime.datetime(2025, 5, 1),
    datetime.datetime(2025, 5, 29),
    datetime.datetime(2025, 6, 9),
    datetime.datetime(2025, 10, 3),
    datetime.datetime(2025, 10, 31),
    datetime.datetime(2025, 12, 25),
    datetime.datetime(2025, 12, 26),
    datetime.datetime(2026, 1, 1),
]

x = int(input("Gib das Jahr an: "))
y = int(input("Gib den Monat an: "))
z = int(input("Gib den Tag an: "))

datum = datetime.datetime(x, y, z)
datum2 = datum.strftime("%d.%m.%Y")


def feiertag(date):
    if date in feiertage:
        print(f"An dem {datum2} hast du keinen Unterricht, es ist ein Feiertag")


# Winterferien 2024
if datum >= datetime.datetime(2024, 12, 24) and datum <= datetime.datetime(2025, 1, 1):
    feiertag(datum)
    print(
        f"An dem {datum2} hast du Winterferien, der Unterricht beginnt wieder am: 2025.01.02"
    )
# Osterferien 2025
elif datum >= datetime.datetime(2025, 4, 18) and datum <= datetime.datetime(
    2025, 4, 21
):
    feiertag(datum)
    print(
        f"An dem {datum2} hast du Osterferien, der Unterricht beginnt wieder am: 2025.04.22"
    )
# Sommerferien 2025
elif datum >= datetime.datetime(2025, 8, 11) and datum <= datetime.datetime(
    2025, 8, 19
):
    feiertag(datum)
    print(
        f"An dem {datum2} hast du Sommerferien, der Unterricht beginnt wieder am: 2025.08.20"
    )
# Winterferien 2025
elif datum >= datetime.datetime(2025, 12, 24) and datum <= datetime.datetime(
    2026, 1, 1
):
    feiertag(datum)
    print(
        f"An dem {datum2} hast du Winterferien, der Unterricht beginnt wieder am: 2026.01.02"
    )
# Feiertage
elif datum in feiertage:
    print(f"An dem {datum2} hast du keinen Unterricht, es ist ein Feiertag")
else:
    print(f"An dem {datum2} hast du Unterricht!")
