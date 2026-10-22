def my_long_word(chiffre, phrase):
    resultat = ""
    mot = ""
    for caractere in phrase + " ":
        if caractere != " ":
            mot = mot + caractere
        else:
            longueur = 0
            for lettre in mot:
                longueur = longueur + 1
            if longueur > chiffre:
                resultat = resultat + mot + " "
            mot = ""
    return resultat.strip()
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, phrase))