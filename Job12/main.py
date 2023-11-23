def insertion_sort(liste):
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > cle:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle
    return liste


liste = [34, 2, 10, 76, 39, 23, 56, 1, 28, 67]
insertion_sort(liste)
print(liste)