def separer(L):
    """
    Sépare les nombres négatifs, nuls et positifs d'une liste d'entiers.

    Cette fonction prend une liste d'entiers `L` et retourne une nouvelle liste `LSEP`
    de la même longueur, où :
    - Les nombres négatifs sont placés à gauche.
    - Les nombres nuls (0) sont placés au centre.
    - Les nombres positifs sont placés à droite.

    Les éléments sont placés dans l'ordre de leur apparition dans la liste d'origine
    mais ne sont pas triés entre eux dans chaque section (négatifs, nuls, positifs).

    Paramètres:
        L (list of int): Liste d'entiers à séparer.

    Retourne:
        list of int: Nouvelle liste `LSEP` avec les nombres négatifs à gauche, 
                     les zéros au centre, et les nombres positifs à droite.
    """
    LSEP = [0] * len(L)  
    gauche = 0             
    droite = len(L) - 1   
    for num in L:        
        if num < 0:      
            LSEP[gauche] = num
            gauche += 1
        elif num > 0:    
            LSEP[droite] = num
            droite -= 1
    return LSEP

# Exemples d'utilisation
print(separer([3, -2, 0, 1, -5, 0, 4, -1]))  
print(separer([0, 0, 0]))                   
print(separer([-1, 1, -2, 2, 0]))  
         
