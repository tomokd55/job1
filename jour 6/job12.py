def trier_croissant(L):
    n = 0
    for nombre in L:
        n = n + 1
    for i in range(n):
        for j in range(n - 1):
            if L[j] > L[j + 1]:
                temporaire = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temporaire
    return L
L = [8, 24, 3, 48, 2, 16, 9, 7]
print("Liste triée :", trier_croissant(L))