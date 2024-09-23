"""
FABBRI Yohann
12 septembre 2024
"""


import numpy as np


def matriceAdjacence(S:list, A:list) -> object:
    """
    Crée la matrice d'adjacence pour un graphe orienté donné par ses sommets et ses arcs.
    
    :param S: Liste des sommets.
    :param A: Liste des arcs, chaque arc étant un tuple (i, j) avec i et j appartenant à S.
    :return: Matrice d'adjacence sous forme d'un array 2D de NumPy.
    """
    n = len(S)
    matrice_adj = np.zeros((n, n), dtype=int)
    for (i, j) in A:
        matrice_adj[i, j] = 1
    return matrice_adj


def matriceAdjacencePond(S:list, A:list) -> object:
    """
    Génère une matrice d'adjacence pondérée à partir d'une liste de sommets et d'arcs pondérés.

    Cette fonction crée une matrice d'adjacence pondérée sous forme d'un tableau NumPy à deux dimensions. 
    Les éléments de la matrice représentent les poids des arcs entre les sommets. 

    :param S: Liste des sommets, représentés par des nombres (ex: [0, 1, 2]).
    :param A: Liste des arcs pondérés, chaque arc est un triplet (i, j, poids) où `i` et `j` sont les sommets 
              connectés et `poids` est la valeur de l'arc.
    :return: Une matrice d'adjacence pondérée sous forme d'un tableau NumPy à deux dimensions.
    """
    n = len(S)
    matrice_adj = np.zeros((n, n), dtype=int)
    for (i, j, poids) in A:
        matrice_adj[i, j] = poids
    return matrice_adj


def lireMatriceFichier(nomfichier:str) -> object:
    """
    Lit une matrice carrée à partir d'un fichier et retourne la matrice sous forme d'un array 2D de NumPy.
    
    :param nomfichier: Nom du fichier contenant la matrice.
    :return: Matrice carrée sous forme d'un array de NumPy.
    """
    return np.loadtxt(nomfichier)


def tousLesSommets(mat:object) -> list:
    """
    Retourne une liste contenant tous les indices des sommets du graphe 
    défini par la matrice d'adjacence `mat`.

    :param mat: Matrice d'adjacence du graphe (array NumPy 2D).
    :return: Liste des indices des sommets.
    """
    np.loadtxt(mat)
    file = open(mat)
    line = file.readline()
    sommets = line.split()
    sommets[0] = sommets[0][1:]
    file.close()
    return sommets


def listeArcs(mat:object) -> list:
    """
    Retourne la liste des arcs (i, j) du graphe défini par la matrice d'adjacence `mat`.

    :param mat: Matrice d'adjacence du graphe (array NumPy 2D).
    :return: Liste des tuples (i, j) représentant les arcs du graphe.
    """
    reseau = np.loadtxt(mat)
    lst_arcs = []
    for i in range(len(reseau)):
        for j in range(len(reseau)):
            if reseau[i,j] > 0:
                lst_arcs.append((i,j))
    return lst_arcs


def matriceIncidence(mat:object) -> object:
    """
    Retourne la matrice d'incidence associée au graphe défini par la matrice d'adjacence `mat`.

    :param mat: Matrice d'adjacence du graphe (array NumPy 2D).
    :return: Matrice d'incidence (array NumPy 2D).
    """
    # Liste des arcs (i, j) où il y a un arc de i vers j
    arcs = [(i, j) for i in range(mat.shape[0]) for j in range(mat.shape[1]) if mat[i, j] != 0]

    num_sommets = mat.shape[0]
    num_arcs = len(arcs)

    incidence_matrix = np.zeros((num_sommets, num_arcs), dtype=int)
    for index, (i, j) in enumerate(arcs):
        incidence_matrix[i, index] = 1  
        incidence_matrix[j, index] = -1   

    return incidence_matrix


def est_voisin(mat:object, S:int, V:int) -> bool:
    """
    Vérifie si deux sommets S et V sont voisins dans le graphe défini par la matrice d'adjacence `mat`.

    :param mat: Matrice d'adjacence du graphe (array NumPy 2D).
    :param S: Sommet de départ (indice de ligne).
    :param V: Sommet d'arrivée (indice de colonne).
    :return: Booléen indiquant si S et V sont voisins.
    """
    reseau = np.loadtxt(mat)
    if reseau[S,V] and reseau[V,S] > 0:
        return True
    return False


def main():
    # Test de matriceAdjacence
    S = [0, 1, 2]
    A = [(0, 1), (1, 2), (2, 0)]
    print("Matrice d'adjacence:")
    print(matriceAdjacence(S, A))

    # Test de matriceAdjacencePond
    S = [0, 1, 2]
    A = [(0, 1, 5), (1, 2, 3), (2, 0, 2)]
    print("\nMatrice d'adjacence pondérée:")
    print(matriceAdjacencePond(S, A))

    # Test de lireMatriceFichier
    print("\nLecture de la matrice depuis 'Graphe.txt':")
    print(lireMatriceFichier('Graphe.txt'))

    # Test de tousLesSommets
    print("\nTous les sommets:")
    print(tousLesSommets('Graphe.txt'))

    # Test de listeArcs
    print("\nListe des arcs:")
    print(listeArcs('Graphe.txt'))

    # Test de matriceIncidence
    matrice_adjacence = np.array([
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0]
    ])
    print("\nMatrice d'incidence:")
    print(matriceIncidence(matrice_adjacence))

    # Test de est_voisin
    print("\nTest si deux sommets sont voisins:")
    print(est_voisin('Graphe.txt', 6, 7))
    print(est_voisin('Graphe.txt', 2, 4))

if __name__ == "__main__":
    main()