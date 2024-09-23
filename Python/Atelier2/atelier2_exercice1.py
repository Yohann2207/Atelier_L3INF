def somme_indices(L:list)->int:
    """boucle for avec les indices"""
    somme = 0
    for i in range(len(L)):
        somme += L[i]
    return somme

def somme_elements(L:list)->int:
    """boucle for avec les éléments"""
    somme = 0
    for e in L:
        somme += e
    return somme

def somme_while(L:list)->int:
    """boucle while"""
    somme = 0
    i = 0
    while i < len(L):
        somme += L[i]
        i += 1
    return somme

print(somme_indices([1,2,3]))
print(somme_elements([1,2,3]))
print(somme_while([1,2,3]))

#La version la plus adaptée est la boucle for basée sur les éléments

def moyenne(L:list)->float:
    if not L:  
        return 0
    return sum(L) / len(L)  

def nb_sup_indices(L:list, e:int)->int:
    count = 0
    for i in range(len(L)):  
        if L[i] > e:
            count += 1
    return count

def nb_sup_elements(L:list, e:int)->int:
    count = 0
    for element in L:  
        if element > e:
            count += 1
    return count

def moy_sup(L:list, e:int)->float:
    sup_elements = [x for x in L if x > e]
    if not sup_elements:
        return 0
    return sum(sup_elements) / len(sup_elements)

def val_max(L:list)->float:
    if not L:  
        return None  
    max_value = L[0]  
    for element in L:
        if element > max_value:
            max_value = element  
    return max_value

def ind_max(L:list)->int:
    if not L:  
        return 0 
    max_index = 0  
    for i in range(len(L)): 
        if L[i] > L[max_index]:
            max_index = i  
    return max_index

def test_exercice1(): 
    print("TEST SOMME") 
    #test liste vide 
    print("Test liste vide : ", somme_elements([])) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 11111 : ", somme_elements(lst2test1))
    lst2test2=[8,8]
    print("Test moyenne 8 : ", moyenne(lst2test2))
    lst2test3=[1,2,3,4,5,6,7,8]
    print("Test valeur sup : ", nb_sup_indices(lst2test3,4))
    print("Test valeur sup : ", nb_sup_elements(lst2test3,4))
    lst2test4=[1,2,3,4,5,5]
    print("Test moyenne des valeurs supérieurs : ", moy_sup(lst2test4,4))
    lst2test5=[1,2,3,4,9,6,7,8]
    print("Test valeur max : ", val_max(lst2test5))
    print("Test indice max : ", ind_max(lst2test5))

test_exercice1()

