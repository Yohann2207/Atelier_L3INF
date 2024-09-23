"""
FABBRI Yohann
12 septembre 2024
"""


import numpy as np


def my_searchsorted(liste: object, element: int) -> int:
  """
    Recherche l'indice où l'élément devrait être inséré dans le tableau trié pour maintenir l'ordre.
    
    :param table: Tableau trié
    :param element: Élément à insérer
    :return: Indice où insérer l'élément
  """
  for i in range(len(liste)):
    if liste[i] >= element:
      return i
  return len(liste)


def my_where(tableau: object, valeur: int) -> list:
  """
    Trouve les indices des éléments dans un tableau multidimensionnel égaux à une valeur donnée.

    Cette fonction parcourt tous les éléments d'un tableau NumPy multidimensionnel et retourne 
    une liste de tuples représentant les indices des éléments qui sont égaux à la valeur spécifiée.

    :param tableau: Un tableau NumPy multidimensionnel.
    :param valeur: La valeur à rechercher dans le tableau.
    :return: Une liste de tuples contenant les indices des éléments égaux à `valeur`.
  """
  lst_indices = []
  for tab, e in np.ndenumerate(tableau):
    if e == valeur:
      lst_indices.append(tab)
  return lst_indices


def my_add1(tableA: object, tableB: object) -> object:
    """
    Additionne deux tableaux NumPy de même dimension en utilisant ndenumerate.

    Cette fonction prend en entrée deux tableaux NumPy de même dimension et retourne un nouveau 
    tableau qui est la somme élément par élément des deux tableaux d'entrée. L'addition est effectuée
    en utilisant `ndenumerate` pour itérer sur les indices et les valeurs des éléments.

    :param tableA: Premier tableau NumPy.
    :param tableB: Deuxième tableau NumPy de même dimension que `tableA`.
    :return: Un tableau NumPy résultant de l'addition élément par élément de `tableA` et `tableB`.
    """
    resultat = np.zeros(tableA.shape)
    
    # Utiliser ndenumerate pour itérer sur les éléments
    for index, value in np.ndenumerate(tableA):
        resultat[index] = value + tableB[index]
    return resultat


def my_add2(tableA: object, tableB: object) -> object:
    """
    Additionne deux tableaux NumPy de même dimension en utilisant des boucles for avec range().

    Cette fonction prend en entrée deux tableaux NumPy de même dimension et retourne un nouveau 
    tableau qui est la somme élément par élément des deux tableaux d'entrée. L'addition est effectuée
    en utilisant des boucles `for` imbriquées avec `range()` pour parcourir les indices des éléments.

    :param tableA: Premier tableau NumPy.
    :param tableB: Deuxième tableau NumPy de même dimension que `tableA`.
    :return: Un tableau NumPy résultant de l'addition élément par élément de `tableA` et `tableB`.
    """
    resultat = np.zeros_like(tableA)
    
    for i in range(tableA.shape[0]):
        for j in range(tableA.shape[1]):
            resultat[i,j] = tableA[i,j] + tableB[i,j]
    return resultat


def matrice_trace(matrice: object) -> float:
    """
    Calcule la trace d'une matrice carrée.

    Args:
        matrice (list of list of int/float): Une matrice carrée (liste de listes).

    Returns:
        int/float: La trace de la matrice (somme des éléments de la diagonale principale).
    """
    # Calcul de la trace
    return sum(matrice[i][i] for i in range(len(matrice))) 


def est_symetrique(matrice: object) -> bool:
    """
    Détermine si une matrice est symétrique.

    Args:
        matrice (list of list of int/float): Une matrice carrée (liste de listes).

    Returns:
        bool: True si la matrice est symétrique, False sinon.
    """
    n = len(matrice)
    for i in range(n):
        for j in range(i + 1, n):  # Vérification seulement au-dessus de la diagonale
            if matrice[i][j] != matrice[j][i]:
                return False
    return True


def produit_diagonal(matrice: object) -> float:
    """
    Calcule le produit des éléments de la diagonale principale d'une matrice carrée.

    Args:
        matrice (list of list of int/float): Une matrice carrée (liste de listes).

    Returns:
        int/float: Le produit des éléments de la diagonale principale.
    """
    # Calcul du produit des éléments de la diagonale principale
    produit = 1
    for i in range(len(matrice)):
        produit *= matrice[i][i]
    return produit


def inverse(A: object) -> object:
    """
    Inverse la matrice A, multiplie A par son inverse, et vérifie si le résultat est 
    proche de la matrice identité.

    Args:
        A (ndarray): Une matrice carrée (numpy array).

    Returns:
        bool: True si le produit est proche de la matrice identité, sinon False.
    """
    A_inv=np.linalg.inv(A)
    return(np.dot(A_inv,A))


def main():
    # Test de la fonction my_searchsorted
    arr = np.array([1, 2, 3, 4, 5, 6, 14])
    print("Tests de my_searchsorted:")
    print(my_searchsorted(arr, 4))   # Output: 3
    print(my_searchsorted(arr, 7))   # Output: 6
    print(my_searchsorted(arr, 15))  # Output: 7
    print(my_searchsorted(arr, 0))   # Output: 0
    print()

    # Test de la fonction myWhere
    M = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print("Tests de myWhere:")
    print(my_where(M, 5))  # Output: [(1, 1)]
    print(my_where(M, 10)) # Output: []
    print()

    # Test de la fonction my_add1
    tableA = np.array([[1, 2], [3, 4]])
    tableB = np.array([[5, 6], [7, 8]])
    print("Test de my_add1:")
    print(my_add1(tableA, tableB))  # Output: [[6, 8], [10, 12]]
    print()

    # Test de la fonction my_add2
    print("Test de my_add2:")
    print(my_add2(tableA, tableB))  # Output: [[6, 8], [10, 12]]
    print()

    # Test des opérations de base sur matrices
    print("Matrice M (3x3) avec des valeurs de 1 à 9:")
    print(M)

    M_plus_10 = M + 10
    M_times_2 = M * 2

    print("Matrice M après avoir ajouté 10 à chaque élément:")
    print(M_plus_10)

    print("\nMatrice M après avoir multiplié chaque élément par 2:")
    print(M_times_2)
    print()

    # Extraction de lignes, colonnes, et sous-matrices
    deuxieme_ligne = M[1]
    troisieme_colonne = M[:, 2]
    sous_matrice = M[:2, :2]

    print("Deuxième ligne de la matrice M:")
    print(deuxieme_ligne)

    print("\nTroisième colonne de la matrice M:")
    print(troisieme_colonne)

    print("\nSous-matrice 2x2 du coin supérieur gauche de la matrice M:")
    print(sous_matrice)
    print()

    # Test des fonctions de trace, symétrie, et produit diagonal
    A = np.random.randint(0, 11, size=(4, 4))
    I = np.eye(4)

    print("Matrice A (4x4) avec des valeurs aléatoires entre 0 et 10:")
    print(A)

    print("\nMatrice identité I (4x4):")
    print(I)

    print("Trace de A:")
    print(matrice_trace(A))  

    print("Matrice A symétrisée:")
    A = (A + A.T)
    print(A)

    print("Symétrie de A après symétrisation:")
    print(est_symetrique(A))

    print("Produit diagonal de la matrice identité:")
    print(produit_diagonal(I))

    print("Inverse de A multipliée par A (devrait être proche de la matrice identité):")
    print(inverse(A))

# Appeler la fonction main
if __name__ == "__main__":
    main()
