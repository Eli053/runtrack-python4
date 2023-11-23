def calculate_product(L):
    product = 1
    for i in L:
        if 25 <= i <= 90:
            product *= i
    return product

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

print(calculate_product(L))