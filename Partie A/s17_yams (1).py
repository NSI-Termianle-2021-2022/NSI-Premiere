#####################################################
# Séance #17 - Corrigé du Yams - 17/11/2020         #
#####################################################

"""
Ce programme gère le niveau 3 du DM. Même si l'interface utilisateur est
claire, on n'a pas de réelle interface graphique.


Structures de données utilisées :
- On utilise une liste pour les joueurs (logique : indexation numérique
  simple, nombre variable de joueurs)

- Chaque joueur est représenté par un dictionnaire car les informations à
  stocker sont connues dès le départ. Idem pour la partie. En utilisant des
  types construits, on peut modifier leurs champs (en passant les variables
  représentant ces types à différentes fonctions).

- Les combinaisons sont aussi représentées par un dictionnaire (logique : on
  connaît à l'avance ce que l'on va y mettre). Ce dictionnaire va initialiser
  les combinaisons de chaque joueur.

- Comme demandé, on utilise une liste pour la variable répartition.
  Utiliser un dictionnaire était possible mais plus compliqué :
  {1: 2, 6: 1, 2: 1, 4: 1} -> [2, 1, 0, 1, 0, 1]
  La seule différence est que le dictionnaire a des clés qui correspondent au
  dé, alors que la liste commence à 0 (donc il faut penser à enlever 1)


Logique du jeu :
- On simule à chaque tour le score POSSIBLE en essayant chaque combinaison
  (kassdédi Marguerite)

- Pour détecter les différents scores, on va utiliser alternativement la
  répartition des dés, ou le tirage (pour les suites par exemple)


Saisie utilisateur et interface :
- Le programme gère quelques saisies utilisateur absurdes, mais pas toutes. À
  vous de trouver celles qui font crasher le programme...

- La limite de 25 lignes est satisfaite ici si l'on enlève les lignes vides
  et les commentaires (recomptez !)

- La règle des 3 "elif" était dure à respecter ici, car il fallait appeler des
  fonctions différentes en fonction de la combinaison cherchée... ce problème
  se résolvait via des fonctions passées comme variables dans un dictionnaire
  (cf. la fonction calcul_score() plus bas)
  (je rappelle qu'utiliser des elif à profusion est souvent le signe d'une
  structure de données manquante)

- Notez que le programme gère un nombre infini d'erreurs de saisie
  utilisateur, de deux façons différentes... cherchez comment !

- Pour effacer une combinaison, on se contente de demander une confirmation
  si le score réalisé est de 0.

- Prenez l'habitude de considérer la saisie avec input() comme un événement
  dangereux, et l'utilisateur comme stupide ou malveillant. Cela vous évitera
  bien des déceptions...

- Remarquez qu'on appelle toujours l'utilisateur par son nom et jamais par
  son numéro (ce qui serait pourtant plus pratique).


Les tests :
- Il faut remplacer MODE = "jeu" par MODE = "test" pour lancer les tests. Les
  tests ne sont pas lancés pendant l'exécution du programme, mais à part.

- On ne teste ici que les lancers de dés, les calculs de score et la relance,
  mais on pourrait pousser plus avant. Certains domaines très sensibles
  (spatial, nucléaire, etc.) demanderaient de tester TOUT le code.

- Il est infiniment plus facile de tester une fonction qui ne fait que
  retourner une valeur (ce qui n'est pas toujours le cas ici). Au maximum,
  organisez votre code pour que toutes vos fonctions retournent des valeurs.

- Les fonctions d'affichage sont difficilement testables, mais cela reste
  possible.

- Notez le ratio de lignes : on a ~300 lignes de code pour ~100 lignes de
  test. Ce ratio est souvent bien inférieur pour des projets bien testés, et
  il n'est pas rare d'écrire plus de tests que de code !

- Coquetterie : les OK s'affichent en vert, car le vert, c'est joli. Utilisez
  de la couleur pour rendre votre interface plus lisible !


Divers :
- On a essayé (au maximum) de respecter une bonne pratique Python d'avoir
  des lignes de moins de 79 caractères.

- Notez l'utilisation de .ljust() pour aligner le texte dans un tableau !

- On a centralisé le nettoyage des input utilisateur dans une fonction
  nettoyer_reponse, que l'on va tester à part. Il n'y a plus de nettoyage de
  chaîne dans le code, ce qui est plus propre.
"""

from random import randint

"""
Quelques constantes (en capitale) en début de jeu nous permettent de
configurer facilement la partie
"""
consts = {"NB_TOUR": 10, "NB_JOUEURS_MAX": 6, "SEUIL_BONUS": 63, "SCORE_BONUS": 35}

MODE = "jeu"
# MODE = "test"


def lancer_de():
    return randint(1, 6)


def tirer_des_tries():
    """Notez la simplicité des compréhensions ! """
    return sorted([lancer_de() for i in range(5)])


def combinaison_vide():
    """
    Chaque joueur commence avec la même structure.
    Combinaison non-jouée : chaîne vide
    Combinaison éliminée : score de 0
    On copiera ensuite cette structure dans chaque joueur avec .copy()
    """
    return {
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "Brelan": "",
        "Carré": "",
        "Full": "",
        "Petite suite": "",
        "Grande suite": "",
        "Yams": "",
        "Chance": "",
    }


def creer_partie():
    joueurs = []
    while True:
        nb_joueurs = int(input("Combien de joueurs ? "))
        if 1 < nb_joueurs <= consts["NB_JOUEURS_MAX"]:
            break
        print("Nombre de joueurs invalide : {}".format(nb_joueurs))

    """Chaque nouveau joueur est initialisé de la même façon... sauf son id"""
    for i in range(nb_joueurs):
        nouveau_joueur = {
            "id": i,
            "nom": "",
            "score": 0,
            "bonus": 0,
            "combinaisons": combinaison_vide().copy(),
        }
        nouveau_joueur["nom"] = input(
            "Joueur {}, quel est votre nom ? ".format(i)
        ).strip()
        joueurs.append(nouveau_joueur)

    partie = {
        "en_cours": True,
        "nb_joueurs": len(joueurs),
        "tour": 1,
        "tour_joueur": -1,
    }
    """Notez ce magnifique double retour avec un tuple, bien pratique !"""
    return joueurs, partie


def score_brelan(repartition):
    """
    Les fonctions de calcul de score sont beaucoup plus faciles à écrire
    avec la répartition des dés qu'avec le tirage brut.
    Attention, le carré et le yam sont aussi des brelans, d'où le >=
    """
    for i in range(6):
        if repartition[i] >= 3:
            return 3 * (i + 1)
    return 0


def score_carre(repartition):
    """Attention, le yam est aussi un carré, d'où le >="""
    for i in range(6):
        if repartition[i] >= 4:
            return 4 * (i + 1)
    return 0


def score_full(repartition):
    """Pour le full, on teste la présence simultanée des valeurs 3 et 2"""
    if 3 in repartition and 2 in repartition:
        return 25
    return 0


def score_petite_suite(tirage_trie):
    """
    Pour la suite, utiliser le tirage brut est beaucoup plus simple
    """
    if tirage_trie == [1, 2, 3, 4, 5]:
        return 30
    return 0


def score_grande_suite(tirage_trie):
    if tirage_trie == [2, 3, 4, 5, 6]:
        return 40
    return 0


def score_yams(repartition):
    for i in range(6):
        if repartition[i] == 5:
            return 50
    return 0


def score_chance(tirage):
    return sum(tirage)


def calcul_score(comb_str, tirage):
    """
    Remarques qu'appeler la chaine avec "_str" nous évite toute confusion : on
    comprend qu'il s'agit de son nom et pas d'une liste.

    On transforme le tirage en liste de répartition avec une
    brave compréhension de listes
    Ex : [2, 6, 5, 3, 3]  => [0, 1, 2, 0, 1, 1]
    """
    repartition = [tirage.count(i) for i in range(1, 7)]

    """L'utilisation de ord() nous permet de dire : si la première lettre de
    la chaîne comb_str est comprise entre les caractères "1" et "6"...
    """
    if ord("1") <= ord(comb_str[0]) <= ord("6"):
        return repartition[int(comb_str) - 1] * int(comb_str)
    else:
        """
        Remarquez la beauté de ce système : on passe dans un dictionnaire
        le nom de la fonction à appeler pour chaque figure.
        Ce système évite d'avoir ce type de code :
        if comb_str == "Brelan":
            return score_brelan(repartition)
        elif comb_str == "Carré":
            return score_carre(repartition)
        elif ...
        """
        fonctions_de_score = {
            "Brelan": (score_brelan, repartition),
            "Carré": (score_carre, repartition),
            "Full": (score_full, repartition),
            "Petite suite": (score_petite_suite, sorted(tirage)),
            "Grande suite": (score_grande_suite, sorted(tirage)),
            "Yams": (score_yams, repartition),
            "Chance": (score_chance, tirage),
        }
        fonction = fonctions_de_score[comb_str]
        """Ex : pour score_yams, cela donnera : score_yams(repartition)"""
        return fonction[0](fonction[1])


"""
Fonctions d'impression
On pourrait envisager de mettre ces fonctions dans un fichier à part.
"""


def imprimer_combinaisons(comb_dict, tirage):
    i = 1
    for combinaison in comb_dict:
        """
        On utilise .ljust() pour avoir une string de 13 caractères en tout,
        quelle que soit la longueur du nom de la combinaison
        """
        c = str(i).ljust(3) + ": " + combinaison.ljust(13)
        if len(str(comb_dict[combinaison])) > 0:
            score = str(comb_dict[combinaison]) + " (fait)"
        else:
            score = calcul_score(combinaison, tirage)
            if score == 0:
                score = "."
        print("{}: {}".format(c, score))
        i += 1
    print("------------------------")


def imprimer_score_joueur(joueur):
    """Idem avec .rjust() pour un padding à droite"""
    str_bonus = str(joueur["bonus"]).rjust(12)
    str_score = str(joueur["score"]).rjust(12)
    print("     BONUS{}".format(str_bonus))
    print("     SCORE{}".format(str_score))


def imprimer_tirage(tirage, lancer):
    print("\nLancer {}:     ".format(lancer), end="")
    for de in tirage:
        print("{} ".format(de), end="")
    print("\n")


def afficher_gagnant(joueurs):
    gagnant = joueurs[0]
    for joueur in joueurs:
        if joueur["score"] + joueur["bonus"] > gagnant["score"] + gagnant["bonus"]:
            gagnant = joueur
    print(
        "Fin de partie. Le joueur {} gagne avec {} points !".format(
            gagnant["nom"], gagnant["score"] + gagnant["bonus"]
        )
    )


def tourner_joueurs(partie, joueurs):
    partie["tour_joueur"] += 1
    if partie["tour_joueur"] >= partie["nb_joueurs"]:
        partie["tour_joueur"] = 0
        partie["tour"] += 1

    if partie["tour"] >= consts["NB_TOUR"]:
        partie["en_cours"] = False
    else:
        """
        Pour aller chercher le nom du joueur, il faut récupérer l'indice du
        joueur dans partie, puis le nom de ce joueur
        """
        print(
            "\n\n ---* Tour {} - {} joue *---\n".format(
                partie["tour"], joueurs[partie["tour_joueur"]]["nom"]
            )
        )


def traiter_relance(tirage, reponse):
    reponse = nettoyer_reponse(reponse)
    if reponse == "N":
        return "N"

    """
    Si on n'a pas répondu "N" ou "n", on relance une seule fois les dés
    choisis. On utilise set() pour enlever les doublons de réponses :
    "33353335533" -> "35"
    """
    for de in "".join(set(reponse)):
        if ord("1") <= ord(de) <= ord("5"):
            tirage[int(de) - 1] = lancer_de()
        else:
            print('Saisie "{}" non-reconnu'.format(de))

    return "Y"


def appliquer_choix(joueur, tirage, comb_str):
    score = calcul_score(comb_str, tirage)

    if score == 0:
        """Si le choix revient à un score de 0, on demande une confirmation"""
        reponse = nettoyer_reponse(
            input("Vous allez barrer {}, êtes-vous sûr ? (y/n)".format(comb_str))
        )
        if reponse != "Y":
            return choisir_case(joueur, tirage, tour_joueur)

    print("Vous avez retenu le {} : {} points.".format(comb_str, score))
    joueur["combinaisons"][comb_str] = score
    joueur["score"] += score

    """
    On calcule le bonus pour les séries de 1, de 2... :
    Si l'on dépasse un certain score avec ces combinaisons, alors on ajoute
    un bonus au joueur (ce bonus est stocké à part).

    Pour ne retenir que les scores sur les combinaisons d'entiers, on crée
    une compréhension de listes qui ne sélectionne :
      - que les clés ayant une longueur de 1
      - que les valeurs numériques (attention aux chaînes nulles ! "")
    """
    s = [
        score
        for comb, score in joueur["combinaisons"].items()
        if len(comb) == 1 and len(str(score)) > 0
    ]
    if sum(s) > consts["SEUIL_BONUS"] and joueur["bonus"] == 0:
        joueur["bonus"] = consts["SCORE_BONUS"]


def choisir_case(joueur, tirage, tour_joueur):
    """
    On tente de convertir la réponse en entier. Si cela échoue, on demande
    de refaire une saisie. On utilise try... catch... pour empêcher au
    programme de crasher (cf. le chapitre 20 du cours Python)
    """
    try:
        reponse = nettoyer_reponse(
            input("{}, quel score choisir ? (1-13) ".format(joueur["nom"]))
        )
        choix = int(reponse)
    except ValueError:
        print("Vous devez saisir un entier entre 1 et 13.")
        return choisir_case(joueur, tirage, tour_joueur)

    if 0 < choix < 14:
        comb_str = list(joueur["combinaisons"].keys())[choix - 1]
        if len(str(joueur["combinaisons"][comb_str])) > 0:
            print("Le {} a déjà été jouée.".format(comb_str))
            return choisir_case(joueur, tirage, tour_joueur)
        appliquer_choix(joueur, tirage, comb_str)
    else:
        print("Vous devez choisir un score entre 1 et 13.")
        return choisir_case(joueur, tirage, tour_joueur)


def nettoyer_reponse(str_brut):
    """
    On enlève les espaces de la chaîne avec .replace(), puis
    on la passe en majuscule : cela nous évite de tester "n" et "N"

    En anglais, on utilisera souvent "sanitize_input"
    """
    return str_brut.replace(" ", "").upper()


def proposer_relances(joueurs, partie, tirage):
    """Première relance"""
    reponse = nettoyer_reponse(
        input(
            "{}, quel dé relancer ? (N pour garder) ".format(
                joueurs[partie["tour_joueur"]]["nom"]
            )
        )
    )

    """
    On évite de demander deux fois de garder son lancer :
    si on a répondu N à la première relance, on saute au choix de la case
    """
    if reponse != "N":
        lancer = 2
        traiter_relance(tirage, reponse)
        imprimer_tirage(tirage, lancer)
        reponse = nettoyer_reponse(
            input(
                "{}, quel dé relancer ? (N pour garder) ".format(
                    joueurs[partie["tour_joueur"]]["nom"]
                )
            )
        )
        if reponse != "N":
            lancer += 1
            traiter_relance(tirage, reponse)

        imprimer_combinaisons(joueurs[partie["tour_joueur"]]["combinaisons"], tirage)
        imprimer_score_joueur(joueurs[partie["tour_joueur"]])
        imprimer_tirage(tirage, lancer)


def yams():
    (joueurs, partie) = creer_partie()
    tourner_joueurs(partie, joueurs)

    while partie["en_cours"]:
        tirage = tirer_des_tries()
        imprimer_combinaisons(joueurs[partie["tour_joueur"]]["combinaisons"], tirage)
        imprimer_score_joueur(joueurs[partie["tour_joueur"]])
        imprimer_tirage(tirage, lancer=1)
        proposer_relances(joueurs, partie, tirage)
        choisir_case(joueurs[partie["tour_joueur"]], tirage, partie["tour_joueur"])
        tourner_joueurs(partie, joueurs)

    afficher_gagnant(joueurs)


if MODE == "jeu":
    yams()


"""Ces chaînes servent à colorier du texte, cf. plus bas"""
GREEN = "\033[92m"
ENDC = "\033[0m"


def test_lancer_de():
    print("Test lancer_de...", end="")
    """
    On s'assure que les lancers sont bien entre 1 et 6, et que toutes
    les valeurs sont obtenues en simulant 10000 lancers.
    On utilise le mot-clé assert pour s'assurer qu'une condition
    est remplie : assert a == 1 crashe si a est différent de 1
    """
    distribution = {i: 0 for i in range(1, 7)}
    for i in range(1, 10_000):
        lancer = lancer_de()
        assert lancer in list(range(1, 7))
        distribution[lancer] += 1
    """
    On teste la distribution des dés : chaque face a environ 16,7% de chance
    d'être tirée.
    """
    for i in distribution:
        assert 0.155 < distribution[i] / 10_000 < 0.185
    print(f"{GREEN} OK{ENDC}")


def test_tirer_des_tries():
    print("Test tirer_des...", end="")
    """
    On s'assure que le tirage est bien une liste de dés entre 1 et 6
    """
    for i in range(1, 10_000):
        tirage = tirer_des_tries()
        assert type(tirage) is list
        assert min(tirage) >= 1
        assert max(tirage) <= 6
    print(f"{GREEN} OK{ENDC}")


def test_score_brelan():
    print("Test score_brelan...", end="")
    brelan_ko_1 = [2, 0, 0, 2, 1, 0]
    """Test : on a bien une répartition valide de 5 dés"""
    assert sum(brelan_ko_1) == 5
    """Test : sans brelan, le score est de 0"""
    assert score_brelan(brelan_ko_1) == 0

    brelan_ko_2 = [0, 0, 2, 0, 2, 1]
    assert sum(brelan_ko_2) == 5
    assert score_brelan(brelan_ko_2) == 0

    """Un full est aussi un brelan"""
    brelan_ok_1 = [0, 0, 2, 0, 3, 0]
    assert sum(brelan_ok_1) == 5
    assert score_brelan(brelan_ok_1) == 3 * 5

    brelan_ok_2 = [1, 3, 0, 1, 0, 0]
    assert sum(brelan_ok_2) == 5
    assert score_brelan(brelan_ok_2) == 3 * 2

    """Un carré est aussi un brelan"""
    brelan_ok_3 = [0, 0, 0, 0, 1, 4]
    assert sum(brelan_ok_3) == 5
    assert score_brelan(brelan_ok_3) == 3 * 6
    print(f"{GREEN} OK{ENDC}")


def test_calcul_score_series():
    print("Test calcul_score 1...", end="")
    assert calcul_score("1", [5, 3, 3, 2, 3]) == 0
    assert calcul_score("1", [1, 3, 3, 1, 3]) == 2
    assert calcul_score("2", [5, 3, 3, 2, 3]) == 2
    assert calcul_score("2", [2, 2, 2, 2, 3]) == 8
    assert calcul_score("3", [5, 3, 3, 2, 3]) == 9
    assert calcul_score("3", [5, 1, 1, 2, 6]) == 0
    assert calcul_score("4", [5, 3, 3, 2, 3]) == 0
    assert calcul_score("4", [4, 3, 3, 4, 4]) == 12
    assert calcul_score("4", [4, 4, 4, 4, 4]) == 20
    assert calcul_score("5", [6, 3, 3, 2, 3]) == 0
    assert calcul_score("5", [5, 3, 3, 5, 3]) == 10
    assert calcul_score("6", [6, 6, 4, 1, 1]) == 12
    assert calcul_score("6", [5, 3, 3, 2, 3]) == 0
    print(f"{GREEN} OK{ENDC}")


def test_calcul_score_figures():
    print("Test calcul_score 2...", end="")
    assert calcul_score("Brelan", [5, 3, 3, 2, 3]) == 9
    assert calcul_score("Brelan", [5, 2, 5, 6, 5]) == 15
    assert calcul_score("Brelan", [2, 3, 4, 2, 1]) == 0
    assert calcul_score("Carré", [2, 2, 2, 2, 1]) == 8
    assert calcul_score("Carré", [2, 2, 5, 2, 1]) == 0
    assert calcul_score("Full", [2, 2, 5, 5, 5]) == 25
    assert calcul_score("Full", [2, 2, 5, 5, 1]) == 0
    assert calcul_score("Full", [2, 2, 2, 2, 1]) == 0
    assert calcul_score("Petite suite", [1, 2, 3, 4, 5]) == 30
    assert calcul_score("Petite suite", [2, 5, 3, 4, 1]) == 30
    assert calcul_score("Petite suite", [2, 5, 5, 4, 1]) == 0
    assert calcul_score("Grande suite", [2, 3, 4, 5, 6]) == 40
    assert calcul_score("Grande suite", [2, 6, 3, 4, 5]) == 40
    assert calcul_score("Grande suite", [2, 6, 3, 2, 5]) == 0
    assert calcul_score("Yams", [3, 3, 3, 3, 3]) == 50
    assert calcul_score("Yams", [3, 3, 3, 3, 2]) == 0
    assert calcul_score("Chance", [2, 4, 5, 3, 2]) == 16
    assert calcul_score("Chance", [1, 1, 3, 6, 4]) == 15
    assert calcul_score("Chance", [1, 1, 1, 1, 1]) == 5
    print(f"{GREEN} OK{ENDC}")


def test_traiter_relance():
    print("Test traiter_relance...", end="")

    assert traiter_relance([1, 1, 3, 6, 4], "   n    ") == "N"
    assert traiter_relance([1, 1, 3, 6, 4], "N    ") == "N"
    assert traiter_relance([1, 1, 3, 6, 4], "    N") == "N"

    """On vérifie que seuls les dés demandés changent"""
    avant = [1, 1, 3, 6, 4]
    apres = avant.copy()
    assert traiter_relance(apres, "2") == "Y"
    for i in [0, 2, 3, 4]:
        assert avant[i] == apres[i]

    """On peut saisir des espaces au milieu de la réponse sans problème"""
    avant = [6, 2, 4, 4, 5]
    apres = avant.copy()
    assert traiter_relance(apres, "    2  1122   ") == "Y"
    for i in [2, 3, 4]:
        assert avant[i] == apres[i]
    print(f"{GREEN} OK{ENDC}")


def test_nettoyer_reponse():
    print("Test nettoyer_reponse...", end="")
    assert nettoyer_reponse(" ") == ""
    assert nettoyer_reponse(" y") == "Y"
    assert nettoyer_reponse("y ") == "Y"
    assert nettoyer_reponse("  1 2   3   ") == "123"
    print(f"{GREEN} OK{ENDC}")


def lancer_tests():
    test_lancer_de()
    test_tirer_des_tries()
    test_score_brelan()
    test_calcul_score_series()
    test_calcul_score_figures()
    test_traiter_relance()
    test_nettoyer_reponse()


if MODE == "test":
    lancer_tests()
