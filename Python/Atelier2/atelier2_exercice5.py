




def nb_occurrences(lst:list,e:int)->int:
    cpt=0
    for e_liste in lst:
        if e_liste==e:
            cpt=cpt+1 
    return(cpt)



     
def vitrine(lst:list, nb_emplacements:int)->list: 
    lst_db_occ=doublon(lst)
    vitrine_1=[]
    vitrine_2=[]
    vitrine_globale=[]
    
    print(lst)
    print(lst_db_occ)
    
    for e in lst_db_occ: 
        lst.remove(e) #Enlève la première occurence de e dans lst 
    print(lst)
    print(lst_db_occ)
    for i in range(len(lst)):
        if lst[i] in lst_db_occ : #On traite les doublons (une occurerence dans chaque vitrine )
            vitrine_1.append(lst[i])
            vitrine_2.append(lst[i])
        elif nb_occurrences(lst, lst[i]) > 2 : #Si il y a 3 occurrences ce n'est pas possible 
            vitrine_globale=[]
            return ([])
        elif len(vitrine_1)< nb_emplacements-1 : #Si il reste de la place je mets dans la vitrine 1 
            vitrine_1.append(lst[i])
        elif len(vitrine_2)< nb_emplacements-1 :  #Si il reste de la place je mets dans la vitrine 2
             vitrine_2.append(lst[i])
        else : 
            vitrine_globale=[] #Sinon ce n'est pas possible 
    vitrine_globale.append(vitrine_1)
    vitrine_globale.append(vitrine_2)
    return(vitrine_globale)
        
            
            
   
     

    
            

def doublon(lst:list)->list: 
    lst_double_occ=[]
    for i in range (len(lst)):
        if nb_occurrences(lst, lst[i])==2 : 
            lst_double_occ.append(lst[i])
            
    for i in range (len(lst_double_occ)):
        if i % 2 ==0 :
            lst_double_occ.pop(i) # On a mis les doublons dans liste_double_occ (1 seul) 
    return(lst_double_occ)