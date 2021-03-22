# Somme des entiers entre 2 bornes
# date : 19/03/2021
# auteur : Gwen
val = 0
val2 = 0

# saisie des bornes
val = int(input("Entrez un nombre entier pour commencer = "))
val2 = int(input("Entrez un nombre entier pour finir = "))

somme = 0

# calcul et affichage de la somme
for k in range(val, val2+1):
    somme = somme + k

print("la somme des nombre entier entre ", val," et ", val2, " = ", somme)
