# schreibe eine funktion, den den User nach dem Alter fragt
# und auf der Konsole ausgibt


def useralter():
    alter = int(input("wie alt bist du? "))
    print(alter)


def namekonsole():
    name = input("Wie lautet dein Name?: ")
    print(f"Hallo, {name}")


def namereturn():
    name1 = input("Wie lautet dein Name?: ")
    return name1


namekonsole()

namereturn()
