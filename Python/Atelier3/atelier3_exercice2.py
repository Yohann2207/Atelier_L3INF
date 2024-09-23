def mots_Nlettres(lst_mot:list, n:int) -> list:
    """
    Cette fonction prend une liste de mots (lst_mot) et un entier (n), 
    et retourne une liste de mots qui ont exactement n lettres.
    
    :param lst_mot: Liste de mots
    :param n: Nombre de lettres
    :return: Liste de mots avec exactement n lettres
    """
    return [mot for mot in lst_mot if len(mot) == n]


def commence_par(mot: str, prefixe: str) -> bool:
    """
    Cette fonction vérifie si le mot commence par le préfixe donné.
    
    :param mot: Le mot à vérifier
    :param prefixe: Le préfixe à rechercher
    :return: True si mot commence par prefixe, False sinon
    """
    if len(prefixe) > len(mot):
        return False
    for i in range(len(prefixe)):
        if mot[i] != prefixe[i]:
            return False
    return True


def finit_par(mot: str, suffixe: str) -> bool:
    """
    Cette fonction vérifie si le mot se termine par le suffixe donné.
    
    :param mot: Le mot à vérifier
    :param suffixe: Le suffixe à rechercher
    :return: True si mot se termine par suffixe, False sinon
    """
    if len(suffixe) > len(mot):
        return False
    for i in range(1, len(suffixe) + 1):
        if mot[-i] != suffixe[-i]:
            return False
    return True


def finissent_par(lst_mot: list, suffixe: str) -> list:
    """
    Renvoie la liste des mots présents dans lst_mot qui se terminent par le suffixe spécifié.

    Paramètres:
    lst_mot (list): Une liste de mots (chaînes de caractères).
    suffixe (str): Le suffixe à rechercher à la fin de chaque mot.

    Retourne:
    list: Une liste des mots qui se terminent par le suffixe.
    """
    return [mot for mot in lst_mot if finit_par(mot, suffixe)]


def commencent_par(lst_mot: list, prefixe: str) -> list:
    """
    Renvoie la liste des mots présents dans lst_mot qui commencent par le préfixe spécifié.

    Paramètres:
    lst_mot (list): Une liste de mots (chaînes de caractères).
    prefixe (str): Le préfixe à rechercher au début de chaque mot.

    Retourne:
    list: Une liste des mots qui commencent par le préfixe.
    """
    return [mot for mot in lst_mot if commence_par(mot, prefixe)] 


def liste_mots(lst_mot: list, prefixe: str, suffixe: str, n: int) -> list:
    """
    Renvoie la liste des mots présents dans lst_mot qui commencent par le préfixe,
    se terminent par le suffixe et contiennent exactement n lettres.

    Paramètres:
    lst_mot (list): Une liste de mots (chaînes de caractères).
    prefixe (str): Le préfixe à rechercher au début de chaque mot.
    suffixe (str): Le suffixe à rechercher à la fin de chaque mot.
    n (int): Le nombre exact de lettres que chaque mot doit contenir.

    Retourne:
    list: Une liste des mots qui répondent aux critères spécifiés.
    """
    # Filtrer les mots qui commencent par le préfixe
    mots_prefixe = commencent_par(lst_mot, prefixe)
    
    # Filtrer les mots qui se terminent par le suffixe parmi ceux qui commencent par le préfixe
    mots_suffixe = finissent_par(mots_prefixe, suffixe)
    
    # Filtrer les mots qui ont exactement n lettres parmi ceux qui commencent par le préfixe et se terminent par le suffixe
    mots_final = mots_Nlettres(mots_suffixe, n)
    
    return mots_final


def dictionnaire(fichier: str) -> list:
    """
    Lit un fichier texte dont chaque ligne contient un mot et renvoie la liste des mots présents dans le fichier.

    Paramètres:
    fichier (str): Le nom du fichier texte à lire.

    Retourne:
    list: Une liste des mots présents dans le fichier.
    """
    mots = []
    try:
        with open(fichier, 'r') as f:
            mots = [ligne.strip() for ligne in f]
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' n'a pas été trouvé.")
    except IOError as e:
        print(f"Une erreur est survenue lors de l'ouverture du fichier : {e}")
    return mots


mots_dans_fichier = dictionnaire("littre.txt")
print(mots_dans_fichier)


def test_fonctions():
    assert mots_Nlettres(["jouer", "jour", "chat", "chien"], 4) == ["jour", "chat"], "Test échoué pour mots_Nlettres"
    assert mots_Nlettres(["ordinateur", "ordinateur"], 10) == ["ordinateur", "ordinateur"], "Test échoué pour mots_Nlettres"

    assert commence_par("ordinateur", "ordi") == True, "Test échoué pour commence_par avec 'ordi'"
    assert commence_par("ordinateur", "table") == False, "Test échoué pour commence_par avec 'table'"
    assert commence_par("parapluie", "para") == True, "Test échoué pour commence_par avec 'para'"
    
    assert finit_par("ordinateur", "teur") == True, "Test échoué pour finit_par avec 'teur'"
    assert finit_par("ordinateur", "table") == False, "Test échoué pour finit_par avec 'table'"
    assert finit_par("fichier.txt", ".txt") == True, "Test échoué pour finit_par avec '.txt'"

    mots1 = ["ordinateur", "fichier.txt", "document.pdf", "image.jpeg", "rapport.docx", "presentation.txt"]
    assert finissent_par(mots1, ".txt") == ["fichier.txt", "presentation.txt"], "Test échoué pour finissent_par"

    mots2 = ["ordinateur", "oranger", "omelette", "objectif", "bureautique"]
    assert commencent_par(mots2, "or") == ["ordinateur", "oranger"], "Test échoué pour commencent_par"

    mots3 = ["ordinateur", "oranger", "omelette", "objectif", "bureautique", "orangina"]
    assert liste_mots(mots3, "or", "er", 7) == ["oranger"], "Test échoué pour liste_mots"


test_fonctions()
