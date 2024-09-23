def position_for(lst: list, elt: int) -> int:
    """
    Retourne l'indice de l'entier `elt` dans la liste `lst` en utilisant une boucle for sur les indices.

    Paramètres:
        lst (list of int): La liste dans laquelle chercher l'entier.
        elt (int): L'entier à rechercher dans la liste.

    Retourne:
        int: L'indice de l'entier `elt` dans la liste `lst`, ou -1 si `elt` n'est pas présent.
    """
    for i in range(len(lst)):  
        if lst[i] == elt:  
            return i  
    return -1  

print(position_for([1, 3, 5, 7, 9], 5))
print(position_for([1, 3, 5, 7, 9], 4))

def position_while(lst: list, elt: int) -> int:
    """
    Retourne l'indice de l'entier `elt` dans la liste `lst` en utilisant une boucle while.

    Paramètres:
        lst (list of int): La liste dans laquelle chercher l'entier.
        elt (int): L'entier à rechercher dans la liste.

    Retourne:
        int: L'indice de l'entier `elt` dans la liste `lst`, ou -1 si `elt` n'est pas présent.
    """
    i = 0 
    while i < len(lst):  
        if lst[i] == elt:  
            return i  
        i += 1  
    return -1

print(position_while([1, 3, 5, 7, 9], 5))
print(position_while([1, 3, 5, 7, 9], 4))

def nb_occurrences(lst: list, e: int) -> int:
    """
    Compte le nombre d'occurrences de l'entier `e` dans la liste `lst`.

    Paramètres:
        lst (list of int): La liste dans laquelle compter les occurrences.
        e (int): L'entier dont on veut compter les occurrences.

    Retourne:
        int: Le nombre d'occurrences de `e` dans `lst`.
    """
    count = 0  
    for element in lst:  
        if element == e:  
            count += 1  
    return count 

print(nb_occurrences([1, 3, 5, 3, 7, 9, 3], 3))
print(nb_occurrences([1, 3, 5, 7, 9], 4))

def est_triee_for(lst: list) -> bool:
    """
    Vérifie si la liste `lst` est triée par ordre croissant en utilisant une boucle for.

    Paramètres:
        lst (list of int): La liste à vérifier.

    Retourne:
        bool: True si la liste est triée par ordre croissant, False sinon.
    """
    for i in range(len(lst) - 1):  
        if lst[i] > lst[i + 1]: 
            return False  
    return True  

print(est_triee_for([1, 2, 3, 4, 5]))
print(est_triee_for([1, 3, 2, 4, 5]))

def est_triee_while(lst: list) -> bool:
    """
    Vérifie si la liste `lst` est triée par ordre croissant en utilisant une boucle while.

    Paramètres:
        lst (list of int): La liste à vérifier.

    Retourne:
        bool: True si la liste est triée par ordre croissant, False sinon.
    """
    i = 0  
    while i < len(lst) - 1:  
        if lst[i] > lst[i + 1]:  
            return False  
        i += 1  
    return True  

print(est_triee_while([1, 2, 3, 4, 5]))
print(est_triee_while([1, 3, 2, 4, 5]))

def position_tri(lst: list, e: int) -> int:
    """
    Retourne l'indice de l'entier `e` dans une liste triée `lst` en utilisant la recherche dichotomique.

    Paramètres:
        lst (list of int): La liste triée dans laquelle chercher l'entier.
        e (int): L'entier à rechercher dans la liste.

    Retourne:
        int: L'indice de `e` dans `lst`, ou -1 si `e` n'est pas présent.

    """
    debut = 0
    fin = len(lst) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if lst[milieu] == e:
            return milieu
        elif lst[milieu] < e:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1

print(position_tri([1, 3, 5, 7, 9], 3))
print(position_tri([1, 3, 5, 7, 9], 4))

def a_repetitions(lst: list) -> bool:
    """
    Détecte s'il y a des répétitions d'entiers dans la liste `lst`.

    Paramètres:
        lst (list of int): La liste à vérifier.

    Retourne:
        bool: True si la liste contient des répétitions, False sinon.
    """
    T = []
    i = 0
    while i < len(lst):
        if lst[i] in T:
            return True
        else:
            T.append(lst[i])
        i += 1
    return False

print(a_repetitions([1, 3, 5, 7, 9, 7]))
print(a_repetitions([1, 3, 5, 7, 9]))
