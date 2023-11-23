def my_long_word(num, string):
    # Supprimer les espaces à gauche et à droite
    string = string.strip()

    # Convertir la chaîne en liste de mots
    words = string.split(' ')

    # Initialiser la liste des mots plus longs que le chiffre num
    long_words = []

    # Parcourir les mots
    for word in words:
        count = 0
        # Parcourir les caractères du mot
        for char in word:
            count += 1

        # Si le mot est plus long que le chiffre num, l'ajouter à la liste long_words
        if count > num:
            long_words.append(word)

    # Joindre les mots de la liste long_words en une chaîne de caractères
    result = ' '.join(long_words)

    return result

print(my_long_word(3, " La peur est le chemin vers le côté obscur,la peur mène à la colère,la colère mène à la haine,la haine mène à la souffrance "))