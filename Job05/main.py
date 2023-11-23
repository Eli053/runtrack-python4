L = [10, 20, 30, 40, 50] # Crée une liste nommée "L" d'au moins 5 entiers

print(L[1]) # Afficher la deuxième valeur de la liste (20)

def update_L():
    L[3] = L[2] + L[4] # Remplace L[3] par la somme des cases voisines L[2] & L[4]
    print(L) # Afficher à nouveau le tableau modifié

update_L() # Appeler la fonction pour mettre à jour la liste

print(L[-1]) # Afficher la dernière valeur de la liste (50)