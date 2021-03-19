# saisie de la valeur
val = int(input("Entrez un nombre entier = "))

# affichage de la table de multiplication pour cette valeur
k = 1
while k <= 10:
    print(val, "*", k, "=", (val * k))
    k += 1
