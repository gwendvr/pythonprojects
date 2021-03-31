# Programme nombre premier
# date : 24/03/2020
# auteur : Gwen

# saisie du nombre à tester
val = int(input("entrez un nombre entier > 1 : (0 pour arrêter) "))

while val != 0:

    # initialisations
    diviseur = 2
    premier = True

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

    val = int(input("entrez un nombre entier > 1 : (0 pour arrêter) "))
