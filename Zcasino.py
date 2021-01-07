# Le jeu du ZCasino : la roulette
from random import randrange
from math import ceil

# Déclaration des variables
argent = 100
continuer = True
print("Bienvenue au Zcasino, vous avez actuellement ", argent, "$.")

# On entre la mise
while continuer :
    mise = -1
    while mise < 0 or mise > 49 :
        mise = input("Entrez une mise (entre 0 et 49) : ")
        try :
            mise = int(mise)
        except ValueError :
            print("Il n'y a pas de nombre")
            mise = -1
            continue
        if mise < 0 :
            print("Nombre inférieur à 0")
        if mise > 49 :
            print("Nombre est supérieur à 49")

    # On choisi la somme
    somme = 0
    while somme <= 0 or somme > argent :
        somme = input("Combien voulez-vous mettre : ")

        try :
            somme = int(somme)
        except ValueError :
            print("Il n'y a pas de nombre")
            somme = -1
            continue
        if somme <= 0 :
            print("Nombre inférieur ou égale à 0")
        if somme > argent :
            print("Vous avez cru vous étiez riche ah ah ah, vous n'avais que ", argent, "$")

    # La roulette est en marche
    resultat = randrange(50)
    print("ET LE NUMERO GAGNANT EST ", resultat)
    if resultat == mise :
        print("Bravo vous êtes riche ! vous avez gagné", somme * 3, "$ !")
        argent += somme * 3
    elif resultat % 2 == mise % 2 :
        somme = ceil(somme * 0.5)
        print("Au moins vous avez misé sur la bonne couleur. tu gagnes", somme, "$")
        argent += somme
    else :
        print("Vous avez perdu ...")
        argent -= somme

    # On interrompt la partie si le joueur a perdu
    if argent <= 0 :
        print("Vous avez perdu tout ton argent, quel dommage ! On te met à la porte.")
        input()
        continuer = False
    else :
        # On affiche l'argent du joueur
        print("Tu es toujours en jeu avec", argent, "$")
        sortie = input("Souhaitez-vous quitter le casino (o/n) ? ")
        if sortie == "o":
            continuer = False
