def mot_correspond(mot: str, motif: str) -> bool:
    """
    Vérifie si un mot correspond à un motif donné.
    Un motif peut contenir des jokers représentés par le caractère '.' 
    qui peut remplacer n'importe quelle lettre.

    :param mot: Le mot à vérifier
    :param motif: Le motif avec ou sans jokers '.'
    :return: True si le mot correspond au motif, False sinon
    """
    verif = True

    if len(mot) != len(motif):
        verif = False

    for i in range(len(mot)):
        if motif[i] != '.' and mot[i] != motif[i]:
            verif = False
    
    return verif

print(mot_correspond("tarte", "t..t."))  
print(mot_correspond("cheval", "c..v..l"))  
print(mot_correspond("cheval", "c..v.l"))  


def presente(lettre: str, mot: str) -> int:
    """
    Renvoie l'indice de la première occurrence de la lettre dans le mot.
    Retourne -1 si la lettre n'est pas trouvée.

    :param lettre: La lettre à rechercher
    :param mot: La chaîne de caractères dans laquelle rechercher la lettre
    :return: L'indice de la première occurrence de la lettre ou -1 si elle n'est pas trouvée
    """
    res = -1
    for index in range(len(mot)):
        if mot[index] == lettre:
            res = index
    return res 

print(presente('a', 'banane')) 
print(presente('z', 'bonjour'))  
print(presente('o', 'ordinateur'))  


def mot_possible(mot: str, lettres: str) -> bool:
    """
    Vérifie si le mot peut être formé avec les lettres disponibles en prenant en compte
    les occurrences de chaque lettre.

    :param mot: Le mot à vérifier
    :param lettres: La chaîne de caractères contenant les lettres disponibles
    :return: True si le mot peut être formé, False sinon
    """
    verif = True
    # Convertir la chaîne de lettres en une liste pour pouvoir retirer les lettres trouvées
    lettres_disponibles = list(lettres)

    for lettre in mot:
        index = presente(lettre, lettres_disponibles)
        if index == -1:
            verif = False
        lettres_disponibles.pop(index)
    return verif

print(mot_possible("lapin", "abilnpq"))  
print(mot_possible("cheval", "abilnpq"))  
print(mot_possible("chapeau", "abcehpuv"))  
print(mot_possible("chapeau", "abcehpuva"))  


def mots_Nlettres(lst_mot:list, n:int) -> list:
    """
    Cette fonction prend une liste de mots (lst_mot) et un entier (n), 
    et retourne une liste de mots qui ont exactement n lettres.
    
    :param lst_mot: Liste de mots
    :param n: Nombre de lettres
    :return: Liste de mots avec exactement n lettres
    """
    return [mot for mot in lst_mot if len(mot) == n]


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
    return mots


def mot_optimaux(dico: list, lettres: str) -> list:
    """
    Renvoie la liste des mots de longueur maximale présents dans la liste dico
    que l'on peut former avec les lettres passées en paramètre dans la chaîne de caractères lettres.
    
    :param dico: Liste de mots (chaînes de caractères)
    :param lettres: Chaîne de caractères représentant les lettres disponibles
    :return: Liste des mots de longueur maximale pouvant être formés avec les lettres disponibles
    """
    max_len = len(lettres)

    for longueur in range(max_len, 0, -1):
        # Générer les mots de longueur actuelle
        mots_candidats = mots_Nlettres(dico, longueur)
        # Filtrer les mots pour ne conserver que ceux pouvant être formés avec les lettres disponibles
        mots_valides = [mot for mot in mots_candidats if mot_possible(mot, lettres)]
        
        if mots_valides:
            return mots_valides
    
    # Si aucun mot n'est trouvé, retourner une liste vide
    return []


dico = dictionnaire("littre.txt")
print(dico)

print(mot_optimaux(dico, "arorvibps"))
