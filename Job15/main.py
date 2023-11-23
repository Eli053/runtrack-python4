# Initialisation de la liste
liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Fonction d'arrondi
def arrondi(x):
    return int(x + 0.5)

# Arrondir les nombres de la liste
for i in range(len(liste)) :
    liste[i] = arrondi(liste[i])

# Tri dans l'ordre croissant
for i in range(len(liste)) :
    for j in range(i + 1, len(liste)) :
        if liste[i] > liste[j] :
            liste[i], liste[j] = liste[j], liste[i]

print(liste)