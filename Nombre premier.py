# Programme nombre premier
# date : 24/03/2021
# auteur : Gwenaelle
# initialisations

diviseur = 2
premier = True

# saisie du nombre à tester
val = int(input("entrez un nombre entier > 1 : "))

# boucle sur la recherche d’un diviseur
while premier and diviseur * diviseur <= val:
    if val % diviseur == 0:
        premier = False
    diviseur += 1

# affichage du message correspondant au nombre
if premier:
    print(val, "est premier")
else:
    print(val, "n'est pas premier")
