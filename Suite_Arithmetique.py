# termes d'une suite arithmétique
# programme suite arithmetique
# auteur : Gwenaelle Devriendt

# saisie du premier terme, de la raison et le nombre de termes
u0 = int(input("Entrez le premier terme de la suite = "))
r = int(input("Entrez la raison de la suite = "))
nb = int(input("Entrez le nombre de termes = "))

# initialisation de terme (qui démarre à u0)
terme = u0
somme = 0

# boucle pour afficher les nb premiers termes de la suite
for k in range(0, nb-1):
    print("u", k, " = ", terme)
    somme = somme + terme
    terme = terme + r

# Affichage de la somme des termes
print("La somme des termes de la suite est", somme)
