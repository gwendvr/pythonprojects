# Programme de Cryptage
# Ce programme permet d'avoir un message et de le cypter puis de le décrypter
# Date : 25/03/2021
# Auteur : Gwen

# Demande du message à crypter
msg = input("Quel message voulez-vous crypter ? :")

# Inversion de la moitié du message
part1 = msg[len(msg) // 2:len(msg)]
part2 = msg[0:len(msg) // 2]
inverse = part1 + part2

# Affichage du message inversé
print(" le message inversé est =", inverse)

# Cryptage avec la clé
cle = "cryptographie"
resultat = ""
decalage = "-"

for k in range(0, len(inverse)):
    resultat += chr((ord(inverse[k]) ^ ord(cle[k % len(cle)])) + ord(decalage))

# Affichage du message crypté
print("le message crypté est =", resultat)

# Décryptage du message
for k in range(0, len(resultat)):
    resultat += chr((ord(resultat[k]) - ord(decalage)) ^ ord(cle[k % len(cle)]))

# Réinversion du message pour le remettre dans l'ordre
milieu = len(inverse) // 2
if len(inverse) % 2 != 0:
    milieu += 1
resultat2 = inverse[milieu:] + inverse[:milieu]

# Affichage du message décrypté
print("message d'origine = ", resultat2)
