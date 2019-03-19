from random import choice
import string

"""
1. Saisir longueur mot de passe
"""

longueur_mot_passe = 1

while longueur_mot_passe < 10 or longueur_mot_passe > 20:

    try:
        longueur_mot_passe = int(input("\nSaisir nb. de characteres entre 10 et 20: "))

    except ValueError:
        print("""Vous avez saisie quelque chose d'autre qu'un nombre""")

"""
2. Déclarer les caractères possibles
"""

# lettres
alpha_low = string.ascii_lowercase
alpha_up = string.ascii_uppercase

# chiffres
nombres = [str(x) for x in range(0, 10)]

# symbols
symboles = """` ! " ? $ ? % ^ & * ( ) _ - + = { [ } ] : ; @ ' ~ # | \ < , > . ? /"""
symboles = symboles.split(" ")

"""
3. Generer mot de passe
"""

mot_passe = ""
comptes = {"symbole": 0, "nombre": 0, "alpha_low": 0, "alpha_up": 0}

"""
4. Verifier conditions sont repondus
"""
while 0 in comptes.values():
    for i in range(longueur_mot_passe):
        categories = [alpha_up, alpha_low, nombres, symboles]
        element_choisi = choice(choice(categories))
        mot_passe += str(element_choisi)

    print(mot_passe)

    for element in mot_passe:
        if element in alpha_low:
            comptes["alpha_low"] += 1

        elif element in alpha_up:
            comptes["alpha_up"] += 1

        elif element in nombres:
            comptes["nombre"] += 1

        else:
            comptes["symbole"] += 1

    print(comptes)
