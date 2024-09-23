"""
FABBRI Yohann
12 septembre 2024
"""


def somme_recursive(liste: list) -> float:
    """
    Calcule récursivement la somme des éléments d'une liste.

    Cette fonction prend une liste de nombres en entrée et retourne la somme de ses éléments 
    en utilisant une approche récursive. Si la liste est vide, elle retourne 0.0.

    :param liste: Une liste de nombres (entiers ou flottants).
    :return: La somme des éléments de la liste en tant que flottant.
    """
    if not liste:
        return 0.0
    return liste[0] + somme_recursive(liste[1:])


def factorielle_recursive(nombre: int) -> int:
    """
    Calcule la factorielle d'un nombre de manière récursive.

    :param nombre: Un entier dont on veut calculer la factorielle
    :return: La factorielle de l'entier donné
    """
    if nombre == 0 or nombre == 1:
        return 1
    else:
        return nombre * factorielle_recursive(nombre - 1)


def longueur(lst: list) -> int:
    """
    Calcule récursivement la longueur d'une liste.

    :param lst: La liste dont on veut calculer la longueur
    :return: Un entier représentant la longueur de la liste
    """
    if not lst:
        return 0
    else:
        return 1 + longueur(lst[1:])


def minimum(lst: list) -> int:
    """
    Calcule récursivement l'élément minimum d'une liste.

    :param lst: La liste dont on veut trouver l'élément minimum
    :return: Un entier représentant l'élément minimum de la liste
    """
    if len(lst) == 1:
        return lst[0]
    else:
        min_reste = minimum(lst[1:])
        return lst[0] if lst[0] < min_reste else min_reste


def listPairs(lst: list) -> list:
    """
    Cette fonction prend une liste d'entiers et retourne une nouvelle liste
    contenant uniquement les éléments pairs de la liste d'origine.

    :param lst: Liste d'entiers
    :return: Liste contenant uniquement les éléments pairs
    """
    if not lst:
        return []
    if lst[0] % 2 == 0:
        return [lst[0]] + listPairs(lst[1:])
    else:
        return listPairs(lst[1:])


def concat_list(LL: list) -> list:
    """
    Cette fonction prend une liste (LL) qui peut contenir des sous-listes
    et retourne une liste plate avec tous les éléments non-listes de LL et de ses sous-listes.

    :param LL: Liste pouvant contenir des éléments simples et des sous-listes
    :return: Liste plate constituée des éléments non-listes
    """
    if not LL:  
        return []
    elif type(LL[0]) == list:  
        return concat_list(LL[0]) + concat_list(LL[1:])
    return [LL[0]] + concat_list(LL[1:])


def incluse(liste1: list, liste2: list) -> bool:
    """
    Vérifie récursivement si tous les éléments de liste1 sont présents dans liste2 dans l'ordre,
    mais pas nécessairement de manière consécutive.

    :param liste1: Liste des éléments à rechercher
    :param liste2: Liste dans laquelle on cherche les éléments
    :return: True si liste1 est incluse dans liste2, False sinon
    """
    if not liste1:
        return True
    if not liste2:
        return False
    # Si le premier élément de liste1 est le même que le premier élément de liste2,
    # avancer dans les deux listes
    if liste1[0] == liste2[0]:
        return incluse(liste1[1:], liste2[1:])
    # Sinon, avancer seulement dans liste2
    return incluse(liste1, liste2[1:])


def main():
    # Test de somme_recursive
    print("=== Test de somme_recursive ===")
    print("La somme de [1.0, 2.0, 3.0, 4.0, 5.0] est :", somme_recursive([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: 15.0
    print("La somme de [] est :", somme_recursive([]))  # Output: 0.0

    # Test de factorielle_recursive
    print("\n=== Test de factorielle_recursive ===")
    print("Le factoriel de 5 est :", factorielle_recursive(5))  # Output: 120

    # Test de longueur
    print("\n=== Test de longueur ===")
    print("La longueur de [1, 2, 3, 4, 5] est :", longueur([1, 2, 3, 4, 5]))  # Output: 5
    print("La longueur de [] est :", longueur([]))  # Output: 0
    print("La longueur de ['a', 'b', 'c', 'd'] est :", longueur(['a', 'b', 'c', 'd']))  # Output: 4

    # Test de minimum
    print("\n=== Test de minimum ===")
    print("L'élément minimum de [3, 1, 4, 1, 5, 9, 2] est :", minimum([3, 1, 4, 1, 5, 9, 2]))  # Output: 1
    print("L'élément minimum de [7] est :", minimum([7]))  # Output: 7
    print("L'élément minimum de [10, -2, 0, 3, -5, 8] est :", minimum([10, -2, 0, 3, -5, 8]))  # Output: -5

    # Test de listPairs
    print("\n=== Test de listPairs ===")
    print("Les éléments pairs de [1, 2, 3, 4, 5, 6] sont :", listPairs([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]
    print("Les éléments pairs de [7, 9, 11] sont :", listPairs([7, 9, 11]))  # Output: []
    print("Les éléments pairs de [8, 10, 12] sont :", listPairs([8, 10, 12]))  # Output: [8, 10, 12]

    # Test de concat_list
    print("\n=== Test de concat_list ===")
    print("La liste plate de [[0, 1], [2, 3], [4], [6, 7]] est :", concat_list([[0, 1], [2, 3], [4], [6, 7]]))  # Output: [0, 1, 2, 3, 4, 6, 7]
    print("La liste plate de ['Ceci est ', 'un test ', 'de la ', 'concatenation'] est :", concat_list(["Ceci est ", "un test ", "de la ", "concatenation"]))  # Output: ['Ceci est ', 'un test ', 'de la ', 'concatenation']

    # Test de incluse
    print("\n=== Test de incluse ===")
    print("[] est incluse dans [4, 3] :", incluse([], [4, 3]))  # Output: True
    print("[] est incluse dans [] :", incluse([], []))  # Output: True
    print("[1, 2, 6] est incluse dans [1, 2, 3, 5, 6] :", incluse([1, 2, 6], [1, 2, 3, 5, 6]))  # Output: True
    print("[1, 2, 3] est incluse dans [1, 2] :", incluse([1, 2, 3], [1, 2]))  # Output: False
    print("[1, 2, ..., 10] est incluse dans [1, 2, ..., 10] :", incluse(list(range(1, 11)), list(range(1, 11))))  # Output: True
    print("[1, 2] est incluse dans [] :", incluse([1, 2], []))  # Output: False

# Appeler la fonction main pour tester toutes les fonctions
if __name__ == "__main__":
    main()
