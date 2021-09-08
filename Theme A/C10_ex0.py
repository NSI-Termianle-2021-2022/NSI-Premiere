
d = [15, 1.83, 'Paris']
dico = {"age": 0,"taille": 0, "lieu": 0}
element = 'lieu'

def add_key(d, dico):
    if dico['age'] == 0:
        dico["age"] = d[0]
    else:
        print('la valeur existe déjà dans d[0]')
    if dico["taille"] == 0:
        dico["taille"] = d[1]
    else:
        print('la valeur existe déjà dans d[1]')
    if dico["lieu"] == 0:
        dico["lieu"] = d[2]
    else:
        print('la valeur existe déjà dans d[2]')
    return dico

out_dico = add_key(d, dico)
print(out_dico)

def is_there(d, dico):
    for j in dico.keys():
        if d == j:
            return '{} est présent dans le dico'.format(d)
    return "{} n'est pas présent dans le dico".format(d)

rep_out = is_there(element, dico)
print(rep_out)

