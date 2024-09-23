import random

rep = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ")


if rep != 'O':
    if rep != 'N':
        print("Je n'ai pas compris votre réponse")

#Contre l'ordinateur
if rep == 'O':
    j1 = input("Quel est votre nom ? ")
    print("Bienvenu ", j1 , " nous allons jouer ensemble \n")
    j2 = 'Machine'
p1 = 0 #points du joueur 1
np = 0 #nombre de parties
#la
#Contre un ami
if rep == 'N':
    j1 = input("Quel est votre nom ? ")
    print("Bienvenu ", j1, " nous allons jouer ensemble")
    j2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ", j2, " nous allons jouer ensemble \n")

cont = True
p2 = 0 #point du joueur 2

#condition d'arret
while cont == True:
#la
    #Jeux
    np += 1
    choix1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=j1))
    if choix1 != 'pierre':
        if choix1 != 'papier':
            if choix1 != 'ciseaux':
                if choix1 != 'puit':
                    choix1ok = False
                    print("Je n'ai pas compris votre réponse")
                    while choix1ok == False:
                        print("Joueur ", j1)
                        choix1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
                        choix1ok = True
                        if choix1 != 'pierre':
                            if choix1 != 'papier':
                                if choix1 != 'ciseaux':
                                    if choix1 != 'puit':
                                        choix1ok = False

    if j2 == 'Machine':
        # Ici il faudrait plutôt vérifier que cpo == 'O' autrement
        # il y a un problème si le joueur 2 s'appelle Machine !
        choix2 = ['papier', 'pierre', 'ciseaux', 'puit'][random.randint(0, 3)]

    if j2 != 'Machine':
        print("Joueur", j2)
        choix2 = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
        if choix2 != 'pierre':
            if choix2 != 'papier':
                if choix2 != 'ciseaux':
                    if choix2 != 'puit':
                        j2bon = False
                        print("Je n'ai pas compris votre réponse")
                        while not j2bon:
                            print("Joueur ", j2)
                            choix2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                            j2bon = True
                            if choix2 != 'pierre':
                                if choix2 != 'papier':
                                    if choix2 != 'ciseaux':
                                        if choix2 != 'puit':
                                            j2bon = False

    # On affiche les choix de chacun
    print("Si on récapitule :", j1, choix1, "et", j2, choix2, "\n")

    # On regarde qui a gagné cette manche on calcule les points et on affiche le résultat

    #egalite
    if choix1 == 'papier' and choix2 == 'papier' or choix1 == 'pierre' and choix2 == 'pierre' or choix1 == 'ciseaux' and choix2 == 'ciseaux':
        gagnant = "aucun de vous, vous êtes ex æquo"
        p1 = p1 + 0
        p2 = p2 + 0
        print("le gagnant est", gagnant)
        print("Les scores à l'issue de cette manche sont donc", j1, p1, "et", j2, p2, "\n")

    #joueurs 2 gagne
    if choix1 == 'pierre' and choix2 == 'papier' or choix1 == 'papier' and choix2 == 'ciseaux' or choix1 == 'ciseaux' and choix2 == 'pierre':
        gagnant = j2
        p1 = p1 + 0
        p2 = p2 + 1
        print("le gagnant est", gagnant)
        print("Les scores à l'issue de cette manche sont donc", j1, p1, "et", j2, p2, "\n")

    #joueurs 1 gagne
    if choix1 == 'pierre' and choix2 == 'ciseaux' or choix1 == 'papier' and choix2 == 'pierre' or choix1 == 'ciseaux' and choix2 == 'papier':
        gagnant = j1
        p1 = p1 + 1
        p2 = p2 + 0
        print("le gagnant est", gagnant)
        print("Les scores à l'issue de cette manche sont donc", j1, p1, "et", j2, p2, "\n")

    if np == 1 or np == 2 or np == 3 or np == 4:
        cont = True
    if np == 5:
        cont = False

    if np == 1 or np == 2 or np == 3 or np == 4:
        # On propose de c ou de s'arrêter
        go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(j1, j2))
        if go == 'O': #On continue
            cont = True
        if go == 'N': #On arrete
            cont = False
        if go != 'O' and go != 'N':
            cont = True
            print("Vous ne répondez pas à la question, on continue ")

#condition d'arret
if cont == False:
    print("Merci d'avoir joué ! A bientôt")