def effectuer_convertion(unit1: str, unit2: str, facteur, reverse=False):
    if reverse:
        facteur = 1/facteur
        unit1, unit2 = unit2, unit1

    nombre_a_convertir = input(f"Valeur à convertir (de {unit1} vers {unit2}, 'q' pour quitter): ")
    if nombre_a_convertir == 'q':
        return True
    try:
        nombre_a_convertir_float = float(nombre_a_convertir)
        print(f"{nombre_a_convertir_float} {unit1} = {round(nombre_a_convertir_float*facteur, 2)} {unit2}")
    except ValueError:
        print("ERREUR: vous devez rentrer un nombre valide. Réessayez!")
        return choix_convertion(unit1, unit2, facteur, reverse)
    return False

def choix_convertion(nb_choix):
    choix_str = input(f"Votre choix (entre 1 et {index}): ")
    try:
        choix_int = int(choix_str)
        if not 1 <= choix_int <= nb_choix:
            print(f"ERREUR: vous devez rentrer un nombre entre 1 et {nb_choix}!!!")
            return choix_convertion(nb_choix)
        return choix_int
    except ValueError:
        print("ERREUR: vous devez rentrer un nombre valide. Réessayez!")
        return choix_convertion(nb_choix)

"""
qui genere des items avec le contraire
ex: 0 ("pouces", "cm", 2.54), 1 ("cm", "pouces", 0.39), ...
"""
convertions = (
    ("POUCES", "CM", 2.54),
    ("KM", "M", 1000)
)

index = 0
print("----- LE CONVERTISSEUR -----")
for convertion in convertions:
    index += 1
    print(f"{index}) {convertion[0]} vers {convertion[1]}")

    index += 1
    print(f"{index}) {convertion[1]} vers {convertion[0]}")


choix = choix_convertion(index)

""" 
définie l'index du tuple convertions 

ex: si choix = 2 alors l'index == 0
"""
index_choix = (choix-1)//2
reverse = choix % 2 == 0

unit1 = convertions[index_choix][0]
unit2 = convertions[index_choix][1]
facteur = convertions[index_choix][2]

while True:
    if effectuer_convertion(unit1, unit2, facteur, reverse):
        break


print("Fin du programme")