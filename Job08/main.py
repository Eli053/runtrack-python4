# Job 08
def somme_valeurs_paires(L):
    somme = 0
    for valeur in L:
        if valeur % 2 == 0:
            somme += valeur
    return somme

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme = somme_valeurs_paires(L)
print(somme)