"""
FABBRI Yohann 
17 septembre 2024
"""

import random as rd
import time
import matplotlib.pyplot as plt


def sort_list(lst:list)->list:
    """
    Trie la liste donnée en utilisant un algorithme de tri par comparaison de base.
    
    Parameters:
    lst (list): La liste à trier.
    
    Returns:
    list: La liste triée dans l'ordre croissant.
    """
    sorted_lst = lst[:]
    for i in range(len(sorted_lst)):
        for j in range(i + 1, len(sorted_lst)):
            if sorted_lst[i] > sorted_lst[j]:
                sorted_lst[i], sorted_lst[j] = sorted_lst[j], sorted_lst[i]
    return sorted_lst


def testTriComparaison():
    taillesListes = [10, 1000, 10000]
    tempsTriPerso = []
    tempsTriPython = []

    for taille in taillesListes:
        liste = list(-i - taille for i in range(taille))

        # Mesurer le temps de la fonction perso
        debutTemps = time.perf_counter()
        sort_list(liste)
        finTemps = time.perf_counter()
        tempsTriPerso.append(finTemps - debutTemps)
        
        # Mesurer le temps du tri intégré de Python
        debutTemps = time.perf_counter()
        sorted(liste)
        finTemps = time.perf_counter()
        tempsTriPython.append(finTemps - debutTemps)

    plt.plot(taillesListes, tempsTriPerso, label='TriPersonnalisé')
    plt.plot(taillesListes, tempsTriPython, label='TriPython')
    plt.xlabel('Taille liste')
    plt.ylabel('Temps')
    plt.title('Comparaison')
    plt.show()


def is_sorted(lst:list)->bool:
    """
    Vérifie si la liste est triée dans l'ordre croissant.
    
    Parameters:
    lst (list): La liste à vérifier.
    
    Returns:
    bool: True si la liste est triée, False sinon.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))


def stupid_sort(lst:list)->list:
    """
    Trie la liste donnée en utilisant un tri stupide (shuffle jusqu'à être trié).
    
    Parameters:
    lst (list): La liste à trier.
    
    Returns:
    list: La liste triée dans l'ordre croissant.
    """
    sorted_lst = lst[:]
    while not is_sorted(sorted_lst):
        rd.shuffle(sorted_lst)
    return sorted_lst


def insertion_sort(lst:list)->list:
    """
    Trie la liste donnée en utilisant l'algorithme du tri par insertion.
    
    Parameters:
    lst (list): La liste à trier.
    
    Returns:
    list: La liste triée dans l'ordre croissant.
    """
    sorted_lst = lst[:]
    for i in range(1, len(sorted_lst)):
        cle = sorted_lst[i]
        j = i - 1
        while j >= 0 and cle < sorted_lst[j]:
            sorted_lst[j + 1] = sorted_lst[j]
            j -= 1
        sorted_lst[j + 1] = cle
    return sorted_lst


def selection_sort(lst:list)->list:
    """
    Trie la liste donnée en utilisant l'algorithme du tri par sélection.
    
    Parameters:
    lst (list): La liste à trier.
    
    Returns:
    list: La liste triée dans l'ordre croissant.
    """
    sorted_lst = lst[:]
    for i in range(len(sorted_lst)):
        min_idx = i
        for j in range(i + 1, len(sorted_lst)):
            if sorted_lst[j] < sorted_lst[min_idx]:
                min_idx = j
        sorted_lst[i], sorted_lst[min_idx] = sorted_lst[min_idx], sorted_lst[i]
    return sorted_lst


def bubble_sort(lst:list)->list:
    """
    Trie la liste donnée en utilisant l'algorithme du tri à bulles.
    
    Parameters:
    lst (list): La liste à trier.
    
    Returns:
    list: La liste triée dans l'ordre croissant.
    """
    sorted_lst = lst[:]
    for i in range(len(sorted_lst)):
        for j in range(0, len(sorted_lst) - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
    return sorted_lst


def merge(gauche:list, droite:list)->list:
    """
    Fusionne deux listes triées en une seule liste triée.
    
    Parameters:
    left (list): La première sous-liste triée.
    right (list): La deuxième sous-liste triée.
    
    Returns:
    list: La liste fusionnée triée.
    """
    res = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            res.append(gauche[i])
            i += 1
        else:
            res.append(droite[j])
            j += 1
    res.extend(gauche[i:])
    res.extend(droite[j:])
    return res


def merge_sort(lst:list)->list:
    """
    Trie la liste donnée en utilisant l'algorithme du tri fusion.
    
    Parameters:
    lst (list): La liste à trier.
    
    Returns:
    list: La liste triée dans l'ordre croissant.
    """
    if len(lst) <= 1:
        return lst
    milieu = len(lst) // 2
    gauche = merge_sort(lst[:milieu])
    droite = merge_sort(lst[milieu:])
    return merge(gauche, droite)


def radix_order_sort(lst:list, exp:int)->list:
    """
    Trie les éléments de la liste basée sur l'ordre des chiffres à une position donnée (exp).
    
    Parameters:
    lst (list): La liste d'entiers à trier.
    exp (int): L'exposant représentant la position du chiffre à utiliser pour trier.
    """
    #Je n'ai pas réussi à faire fonctionner cette fonction.

def radix_sort(lst:list)->list:
    """
    Trie la liste donnée en utilisant l'algorithme du tri par base (radix sort).
    
    Parameters:
    lst (list): La liste à trier.
    
    Returns:
    list: La liste triée dans l'ordre croissant.
    """
    max_val = max(lst)
    exp = 1
    while max_val // exp > 0:
        radix_order_sort(lst, exp)
        exp *= 10
    return lst


def main():
    liste = [2,5,1,3,6,4]
    print("\n--- EXERCICE 6 : Tri personnalisé ---")
    sorted_list = sort_list(liste)
    print(f"Liste triée : {sorted_list}")
    testTriComparaison()

    print("\n--- EXERCICE 7 : Implémentation des tris classiques ---")
    
    # Tri stupide
    print("\nTri stupide :")
    print(stupid_sort(liste))
    
    # Tri par insertion
    print("\nTri par insertion :")
    print(insertion_sort(liste))
    
    # Tri par sélection
    print("\nTri par sélection :")
    print(selection_sort(liste))
    
    # Tri à bulles
    print("\nTri à bulles :")
    print(bubble_sort(liste))
    
    # Tri fusion
    print("\nTri fusion :")
    print(merge_sort(liste))
    
if __name__ == "__main__":
    main()
