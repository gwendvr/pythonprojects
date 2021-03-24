# calcul du nombre de mots dans une phrase
# date : 24/03/2021
# auteur : Gwen

phrase = input("saisir une phrase sans ponctuation, avec un espace entre chaque mot : ")
# ajout d'un espace en fin de phrase pour arrêter la boucle

phrase += " "
nbMots = 0

# boucle pour compter le nombre de mots
while phrase != "":
    positionEspace = phrase.find(" ")
    phrase = phrase[positionEspace + 1:]
    nbMots += 1

# affichage du nombre de mots
print("nombre de mots de la phrase =", nbMots)