def valeur_max_min(L):
    if not L:
        return "La liste est vide."

    valeur_max = max(L)
    valeur_min = min(L)

    return "la valeur max est : " + str(valeur_max) + "\n" + "la valeur min est : " + str(valeur_min)

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(valeur_max_min(L))