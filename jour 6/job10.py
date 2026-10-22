L=[8,24,27,48,2,16,9,102,7,84,91]
produit=1
for valeur in L:
    produit=produit*valeur
    if 25 <= valeur <= 90:
        print(valeur)
print("Le produit est :", produit)