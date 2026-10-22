L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
for i in range(0, 9):
    partie_entiere = int(L[i])
    partie_decimale = L[i] - partie_entiere
    if partie_decimale >= 0.5:
        L[i] = partie_entiere + 1
    else:
        L[i] = partie_entiere
for i in range(0, 9):
    for j in range(0, 8):
        if L[j] > L[j + 1]:
            temporaire = L[j]
            L[j] = L[j + 1]
            L[j + 1] = temporaire
print("Liste arrondie et triée :", L)