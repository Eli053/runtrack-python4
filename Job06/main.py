def swap_first_last(lst):
    if not lst: # si la liste est vide
        return "Erreur: La liste est vide."
    else:
        lst[0], lst[-1] = lst[-1], lst[0] # échanger les valeurs des premières et dernières cases
        return lst

print(swap_first_last([1, 2, 3, 4, 5])) 
print(swap_first_last([5, 2, 3, 4, 1])) 