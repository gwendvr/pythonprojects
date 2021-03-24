# programme addition de puissances
# auteur : Gwenaelle Devriendt

# saisie du nombre de puissance
nb = int(input("Entrez le nombre de puissance de 2 = "))


# initialisations
somme = 0

# boucle pour afficher les nb premiers termes de la suite
for k in range(1, nb+1):
    puissance = pow(2, k)
    somme += puissance
    print("2^", k,"=", puissance)

# Affichage de la somme des termes
print("La somme des puissance de 2 est =", somme)
