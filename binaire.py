# Conversion en binaire
# conversion base 10 et base 2
# Date : 24/03/2021
# Auteur : Gwen

# boucle sur le menu
choix = "Z"
while choix != "Q" and choix != "q":

    # afficher le menu
    print("conversion entier vers binaire .......... 1")
    print("conversion binaire vers entier .......... 2")
    print("quitter ................................. Q")
    choix = input("entrez votre choix ...................... ")

    # conversion entier vers binaire
    if choix == "1":
        binaire = ""
        nb = int(input("entrer un entier = "))

        while nb != 0:
            binaire = str(nb % 2) + binaire
            nb = nb // 2

        print("conversion en binaire = " + binaire)

    # conversion binaire vers entier
    else:

        if choix == "2":
            nb = 0
            k = 0
            binaire = input("entrer un nombre binaire = ")

            while len(binaire) > 0:
                nb += int(binaire[len(binaire)-1:]) * pow(2, k)
                binaire = binaire[: len(binaire)-1]
                k += 1
            print("conversion en base 10 = ", nb)