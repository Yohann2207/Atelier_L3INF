import matplotlib.pyplot as plt

def histo(lst1: list) -> list:
    """
    Crée une liste histogramme représentant la fréquence de chaque valeur dans la liste d'entrée.

    Paramètres:
    lst1 (list): Une liste d'entiers pour laquelle l'histogramme doit être créé.

    Retourne:
    list: Une liste où l'index représente la valeur et l'élément à cet index
          représente la fréquence de cette valeur dans la liste d'entrée.
    """
    max_val = max(lst1)  
    lst2 = [0] * (max_val + 1)  
    for value in lst1:  
        lst2[value] += 1  
    return lst2

print(histo([6, 5, 6, 8, 4, 2, 1, 5]))  

def est_injective(lst: list) -> bool:
    """
    Vérifie si une liste est injective (tous les éléments sont uniques).

    Paramètres:
    lst (list): Une liste d'entiers.

    Retourne:
    bool: True si la liste est injective, sinon False.
    """
    lst_inj = histo(lst)  
    for i in range(len(lst_inj)):
        if lst_inj[i] > 1:
            return False
    return True

print(est_injective([1, 2, 3, 4]))  
print(est_injective([1, 2, 2, 4]))  

def est_surjective(lst: list) -> bool:
    """
    Vérifie si une liste est surjective (toutes les valeurs possibles sont présentes).

    Paramètres:
    lst (list): Une liste d'entiers.

    Retourne:
    bool: True si la liste est surjective, sinon False.
    """
    lst_surj = histo(lst)  
    for i in range(len(lst_surj)):
        if lst_surj[i] == 0:
            return False
    return True

print(est_surjective([1, 2, 3, 4]))  
print(est_surjective([3, 0, 6, 7, 4, 2, 1, 5]))

def est_bijective(lst: list) -> bool:
    """
    Vérifie si une liste est bijective (injective et surjective).

    Paramètres:
    lst (list): Une liste d'entiers.

    Retourne:
    bool: True si la liste est bijective, sinon False.
    """
    return est_injective(lst) and est_surjective(lst)

print(est_bijective([3, 0, 6, 7, 4, 2, 1, 5]))
print(est_bijective([1, 2, 3, 4]))  

def val_max(lst: list) -> float:
    """
    Trouve la valeur maximale dans une liste.

    Paramètres:
    lst (list): Une liste de nombres.

    Retourne:
    float: La valeur maximale dans la liste.
    """
    max_val = lst[0]
    for val in lst:
        if val > max_val:
            max_val = val
    return max_val

def afficheHisto(lst: list) -> str:
    """
    Affiche un histogramme textuel représentant la fréquence de chaque valeur dans la liste.

    Paramètres:
    lst (list): Une liste d'entiers.

    Retourne:
    str: Une chaîne représentant l'histogramme textuel.
    """
    lst_histo = histo(lst)  
    MAXOCC = val_max(lst_histo)
    
    for line in range(MAXOCC, 0, -1):
        for count in lst_histo:
            if count >= line:
                print('#', end=' ') 
            else:
                print(' ', end=' ')  
        print()  
    for i in range(len(lst_histo)):
        print(i, end=' ')
    print()  

afficheHisto([6, 5, 6, 8, 4, 2, 1, 5, 6])

def afficheHistoMatplotlib(lst: list):
    """
    Affiche un histogramme des occurrences dans une liste en utilisant Matplotlib.

    Paramètres:
    lst (list): Une liste d'entiers.

    Retourne:
    None
    """
    plt.hist(lst, bins=range(0, max(lst) + 2), align='left', rwidth=0.8, color='skyblue', edgecolor='black')
    plt.xlabel('Valeurs')
    plt.ylabel('Occurrences')
    plt.title('Histogramme des occurrences dans lst')
    plt.show()

afficheHistoMatplotlib([6, 5, 6, 8, 4, 2, 1, 5, 6])