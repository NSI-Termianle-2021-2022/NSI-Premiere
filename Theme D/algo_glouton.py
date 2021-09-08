def sac_a_dos(contenance: int, objets: dict) -> dict:
    choix = {}
    rapport = []
    clefs = list(objets.keys())
#Calcul de la valeur au kilo de chaque objet
    for i in clefs:
        value = objets[i]
        rapport.append((value[1]/value[0], i))
#Tri des rapports en ordre croissant
    var_bool = True
    while var_bool:
        bon_ordre = 0
        for i in range(len(rapport)-1):
            if rapport[i][0] < rapport[i+1][0]:
                rapport[i], rapport[i+1] = rapport[i+1], rapport[i]
            else:
                bon_ordre += 1
        if bon_ordre == len(rapport)-1:
            var_bool = False
#Choix des objets avec le prix au kilo le plus élevé
    contenace_avant = contenance
    for i in rapport:
        masse_objet = objets[i[1]][0]
        if masse_objet <= contenance:
            contenance -= masse_objet
            choix[i[1]] = objets[i[1]][0]
    return choix

print(sac_a_dos(30, {"A": (13, 700), "B": (12, 400), "C": (8, 300), 'D': (10, 300)}))