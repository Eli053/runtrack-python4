# Initialisation de la liste avec des doublons
liste = [10,20,30,20,10,50,60,40,80,50,40]

# Création d'un dictionnaire à partir de la liste
dictionnaire = {element: 1 for element in liste}

# Conversion du dictionnaire en liste pour supprimer les doublons
liste_sans_doublons = list(dictionnaire.keys())

# Affichage de la liste sans doublons
print(liste_sans_doublons)