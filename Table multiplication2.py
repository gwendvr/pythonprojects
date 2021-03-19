# affichage d'une table de multiplication avec contrôle de saisie
# date : 19/03/2021
# auteur : Gwen

# saisie de la valeur
val = 0
# la valeur est compris entre 1 et 9
while (val < 1) or (val > 9):
    val = int(input("Entrez un nombre entier entre 1 et 9 = "))

    # affichage de la table de multiplication pour cette valeur
for k in range(1, 11):
    print(val, "*", k, "=", (val * k))
