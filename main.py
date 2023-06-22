"""
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"

2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)

3 - Afficher la valeur convertie (et l'unité : cm ou pouces)

- fin du programme.
1 pouce = 2.54 cm

1 cm = 0.394 pouces
"""


def convertion(unite1, unite2, multiplicateur):
    nombre_a_convertir_float = 0
    while nombre_a_convertir_float == 0:
        nombre_a_convertir = input(f"Valeur à convertir (de {unite1} vers {unite2}): ")
        try:
            nombre_a_convertir_float = float(nombre_a_convertir)
        except:
            print("ERREUR: vous devez rentrer un nombre valide. Réessayez!")
        else:
            print(f"{nombre_a_convertir_float} {unite1} = {nombre_a_convertir_float*multiplicateur} {unite2}")


def choix_convertion():
    choix_int = 0
    while choix_int == 0:
        choix_str = input("Votre choix: ")
        try:
            choix_int = int(choix_str)
        except:
            print("ERREUR: vous devez rentrer un nombre valide. Réessayez!")
        else:
            if choix_int < 1 or choix_int > 2:
                print("EEREUR: vous devez choisir 1 ou 2. Réessayez!")
                choix_int = 0
    return choix_int


print("-----LE CONVERTISSEUR-----")
print("1) POUCES VERS CM")
print("2) CM VERS POUCES")
choix = choix_convertion()
quitter_programme = "o"

while not quitter_programme == "n":
    if choix == 1:
        convertion("pouces", "cm", 2.54)
    else:
        convertion("cm", "pouces", 0.394)
    quitter_programme = input("Voulez-vous reconvertir une valeur (n pour quitter)? ")

print("Fin du programme")