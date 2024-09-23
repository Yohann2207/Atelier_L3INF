"""
FABBRI Yohann
17 septembre 2024
"""

import random as rd

def gen_list_random_int(int_nbr=10, int_binf=0, int_bsup=10)->list:
    """Génère et retourne une liste de nombres aléatoires entre 

    Args:
        int_nbr (int, optional): On retourne n nombre dans la liste. Defaults to 10.
        int_binf (int, optional): Le nombre minimum que l'on peut avoir. Defaults to 0.
        int_bsup (int, optional): Le nombre maximum que l'on peut avoir. Defaults to 10.

    Returns:
        list: La liste de nombre aléatoire
    """
    return [rd.randint(int_binf, int_bsup - 1) for i in range(int_nbr)]


def mix_list(list_to_mix:list)->list:
    """Prends une liste en paramètre et la retourne mélangée

    Args:
        list_to_mix (list): La liste que l'on va mélanger

    Returns:
        list: La liste mélanger
    """
    mixed_list = list_to_mix[:]
    
    for i in range(len(mixed_list) - 1, 0, -1):
        j = rd.randint(0, i)
        mixed_list[i], mixed_list[j] = mixed_list[j], mixed_list[i]
    return mixed_list

 
def choose_element_list(liste:list)->int:
    """
    Choisit un élément aléatoire dans une liste
    
    Args:
        liste (list): liste d'éléments

    Returns:
        int: élément qu'on a choisit aléatoirement
    """
    if not liste:
        return [] 
    pos=rd.randint(0, len(liste)-1)
    return(liste[pos])


def extract_elements_list(liste:list, nb_elements:int)->list:
    """
    Renvoyer aléatoirement nb éléments d'une liste
    Args:
        liste (list): liste d'éléments
        nb_elements (int): nb éléments à renvoyer

    Returns:
        list: renvoie une liste de nb élément
    """
    res = []
    lst=liste.copy()
    for i in range(nb_elements):
        element = choose_element_list(lst)
        res.append(element)
        liste.remove(element)
    return res


def main():
    liste = [2,5,1,6,4,3]
    print("\n--- Test de la fonction gen_list_random_int ---")
    lst = gen_list_random_int()
    print(f"Liste aléatoire générée : {lst}")
    
    print("\n--- Test de la fonction mix_list ---")
    mixed_list = mix_list(liste)
    print(f"Liste mélangée : {mixed_list}")
    
    print("\n--- Test de la fonction choose_element_list ---")
    chosen_element = choose_element_list(liste)
    print(f"Élément choisi dans la liste : {chosen_element}")
    
    print("\n--- Test de la fonction extract_elements_list ---")
    extracted_elements = extract_elements_list(liste, 3)
    print(f"Éléments extraits : {extracted_elements}")

if __name__ == "__main__":
    main()
