#Mars Manon Fabbri Yohann L3 ST 
#Atelier de programmation 1 
#Exercice 1
 
def message_imc(imc:float)->str:

    """Evalue notre état corporel.
 
   Args : 

       imc (float) : l'IMC 

   Returns :

       message (str) : l'état corporel

   """

    bornes=[0, 16.5, 18.5,25,30,35,40, float('inf')]

    etats=["Dénutrition", "Maigreur", "Corpulence normale", "Surpoids", "Obsésité modérée", "Obésité sévère", "Obésité morbide"]

    if imc>40:

        message="Obésité morbide"

    else : 

        for i in range(0, 6):

            if imc>bornes[i] and imc<=bornes[i+1]:

                message=etats[i]

    return(message)
 
 
 
def test_imc():

    """Teste la fonction message_imc().
 
   Args : 

   Returns :

   """

    print(message_imc(14))

    print(message_imc(18.5))

    print(message_imc(25))

    print(message_imc(30))

    print(message_imc(35))

    print(message_imc(40))

    print(message_imc(42))

test_imc()