#Mars Manon Fabbri Yohann L3 ST 
#Atelier de programmation 1 
#Exercice 3

import math

def discriminant(a:float,b:float,c:float)->float:
    if a==0:
        print("a doit être différent de 0")
    else : 
        rep=(b*b)-(4*a*c)
    return(rep)


def racine_unique(a:float, b:float)->float:
    if a==0:
        print("a doit être différent de 0")
    else :
        rep=(-b)/(2*a)
    return(rep)



def racine_double(a:float,b:float, delta:float, num:int)->float:
    if num==1 : 
        rep= ((-b+math.sqrt(delta))/2*a)
    elif num==2 :
        rep= ((-b-math.sqrt(delta))/2*a)
    else:
        print("num doit être égal à 1 ou 2")
    return(rep)
        
        
def str_equation(a:float, b:float, c:float)->str:
    a= str(a)
    b=str(b)
    c=str(c)
    if a=="0":
        res=("a doit être différent de 0")
    elif b=="0":
        res= a + "x2+" + c + "=0"
        if c=="0": 
            res=a + "x2=0"  
    elif c=="0": 
        res=a + "x2+" + b + "x=0" 
        if b=="0":
            res= a + "x2-=0"
        
        
    elif a=="1":
        res="x2+" + b + "x+" + c + "=0"
        if b=="1":
            res="x2+" + "x+" + c + "=0"
            
    elif b=="1" : 
        res= a + "x2+" +"x+" + c + "=0" 
        if a=="1":
            res="x2+" + b + "x+" + c + "=0"
            
    else :
        res=a + "x2+" + b + "x+" + c + "=0"
    return(res)




def solution_equation(a:float, b:float, c:float)->str:
    delta=discriminant(a,b,c)
    if delta<0:
        res="Pas de solution réelle pour l'équation " + str_equation(a,b,c)
    elif delta==0 : 
        res= "L'équation " +  str_equation(a,b,c) + " admet une racine simple : x=" + str(racine_unique(a,b))
    else :
        x1=str(racine_double(a,b,delta,1))
        x2=str(racine_double(a,b,delta,2))
        res= "L'équation " +  str_equation(a,b,c) + " admet deux racines réelles : x1= " + x1 + " x2=" + x2
    return(res)

def equation(a:float, b:float, c:float):
    delta=discriminant(a,b,c)
    if delta<0:
        print("Pas de solutions réelles")
    elif delta==0:
        print(racine_unique(a,b))
    else : 
        print (racine_double(a,b, delta, 1))
        print (racine_double (a,b,delta, 2))
        
        

def test_equation():
    print(solution_equation(1,1,1))
    print(solution_equation(1, 0,0))
    print(solution_equation(1,4,3))
    
    