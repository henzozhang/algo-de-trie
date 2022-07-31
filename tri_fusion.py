from random import randint

def tri_fusion(liste_a_trier):
    if len(liste_a_trier) == 1:
        return liste_a_trier
    pivot = len(liste_a_trier) // 2
    liste_gauche = liste_a_trier[:pivot]
    liste_droite = liste_a_trier[pivot:]
    print(liste_gauche)
    print(liste_droite)
    gauche = tri_fusion(liste_gauche)
    droite = tri_fusion(liste_droite)
    return fusion(gauche,droite)

def fusion(liste_gauche, liste_droite):
    resultat = []
    taille_gauche = len(liste_gauche)
    taille_droite = len(liste_droite)
    i  = j = 0
    
    while i < taille_gauche and j < taille_droite:
        if liste_gauche[i] < liste_droite[j]:
            resultat.append(liste_gauche[i])
            i += 1
        else:
            resultat.append(liste_droite[j])
            j += 1
    if i == taille_gauche:
        reste = taille_droite - j
        for _ in range(reste):
            resultat.append(liste_droite[j])
            j += 1
    elif j == taille_droite:
        reste = taille_gauche - i
        for _ in range(reste):
            resultat.append(liste_gauche[i])
            i += 1
    return resultat

liste_test = [randint(0, 100) for _ in range(25)]
print(liste_test)
print(tri_fusion(liste_test))
