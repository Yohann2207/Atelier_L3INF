import random


def places_lettre(ch: str, mot: str) -> list:
    """
    Cette fonction prend un caractère (ch) et une chaîne de caractères (mot), 
    et retourne une liste des indices où le caractère apparaît dans la chaîne.
    Si le caractère n'est pas présent, elle retourne une liste vide.
    
    :param ch: Caractère à rechercher
    :param mot: Chaîne de caractères dans laquelle chercher
    :return: Liste des indices du caractère dans la chaîne
    """
    indices = []  
    index = 0   
    for c in mot:
        if c == ch:  
            indices.append(index)  
        index += 1  
    return indices


def test_places_lettre() -> str:
    ch = input("Entrez une lettre (un seul caractère) : ")
    mot = input("Entrez un mot : ")
    try:
        if len(ch) != 1:
            raise ValueError("Erreur : veuillez entrer un seul caractère.")
        indices = places_lettre(ch, mot)
        if indices:
            print(f"La lettre '{ch}' apparaît aux indices : {indices}")
        else:
            print(f"La lettre '{ch}' n'apparaît pas dans le mot '{mot}'.")
    except ValueError as e:
        print(e)


test_places_lettre()


def outputStr(mot: str, lpos: list) -> str:
    """
    Cette fonction prend une chaîne de caractères (mot) et une liste d'entiers (lpos) représentant 
    les indices des caractères à afficher. Elle retourne une nouvelle chaîne où les caractères à 
    des indices non présents dans lpos sont remplacés par des tirets ('_').
    
    :param mot: La chaîne de caractères d'origine
    :param lpos: Liste des indices des caractères à afficher
    :return: Une chaîne avec des caractères ou des tirets selon les indices
    """
    resultat = ['_'] * len(mot)
    for i in lpos:
        if 0 <= i < len(mot):  
            resultat[i] = mot[i]
    return ' '.join(resultat)


print(outputStr('bonjour', []))          
print(outputStr('bonjour', [0]))         
print(outputStr('bonjour', [0, 1, 4]))   
print(outputStr('bon', [0, 1, 2]))       
print(outputStr('maman', [1, 3]))     
print(outputStr('maman', [0,1,2,3,4]))    


def runGame():
    # Charger la liste des mots depuis un fichier
    lst = build_list("capitales.txt") 
    
    # Construire le dictionnaire des mots par taille
    dictionnaire_mots = build_dict(lst)
    
    print("Choisissez un niveau de difficulté:")
    print("1. Easy (mots de moins de 7 lettres)")
    print("2. Normal (mots de 7 à 8 lettres)")
    print("3. Hard (mots de plus de 8 lettres)")
    
    niveau = input("Entrez le numéro du niveau choisi (1, 2 ou 3): ")
    
    if niveau == '1':
        tailles_possibles = [key for key in dictionnaire_mots.keys() if key < 7]
    elif niveau == '2':
        tailles_possibles = [key for key in dictionnaire_mots.keys() if 6 < key < 9]
    elif niveau == '3':
        tailles_possibles = [key for key in dictionnaire_mots.keys() if key > 8]
    else:
        print("Choix invalide, veuillez sélectionner 1, 2 ou 3.")
        return
    
    if not tailles_possibles:
        print("Aucun mot disponible pour le niveau choisi.")
        return
    
    taille_choisie = random.choice(tailles_possibles)
    
    # Sélectionner un mot aléatoire de la taille choisie
    mot = select_word(dictionnaire_mots, taille_choisie)
    
    print(f"Le mot à deviner a été choisi. Il comporte {taille_choisie} lettres.")
    
    indices_trouves = []
    max_erreurs = 5
    erreurs = 0
    
    dessins_pendu = [
        "|---]",  # C1
        "| O ",   # C2
        "| T ",    # C3
        "|/ \ ",    # C4
        "|_______"   # C5
    ]
    
    print("Mot à deviner :", outputStr(mot, indices_trouves))
    
    while erreurs < max_erreurs:
        lettre = input("Proposez une lettre : ").lower()
        
        if len(lettre) != 1 or not lettre:
            print("Veuillez entrer une seule lettre.")
            continue
        
        # Trouver les indices de la lettre dans le mot
        indices = places_lettre(lettre, mot)
        
        if indices:
            # Ajouter les nouveaux indices trouvés
            indices_trouves.extend(indices)
            
            print("Mot actuel :", outputStr(mot, indices_trouves))
            
            if len(indices_trouves) == len(mot):
                print("Félicitations ! Vous avez trouvé le mot :", mot)
                return
        else:
            erreurs += 1
            print("Lettre incorrecte. Nombre d'erreurs :", erreurs)
            print("Dessin du pendu :\n", '\n'.join(dessins_pendu[:erreurs]))
            print("Mot actuel :", outputStr(mot, indices_trouves))
    
    print("Désolé, vous avez perdu. Le mot était :", mot)


def build_list(fileName: str) -> list:
    """
    Lit un fichier contenant les noms des capitales du monde et retourne une liste de ces noms en minuscules.
    
    :param fileName: Le nom du fichier contenant les capitales du monde.
    :return: Liste des capitales en minuscules.
    """
    capitales = []
    try:
        # Ouvre le fichier en mode lecture
        with open(fileName, "r") as file:
            # Lire toutes les lignes du fichier
            content = file.readlines()
            
            # Pour chaque ligne, séparer par tabulation et convertir en minuscules
            for line in content:
                # Séparer les mots de chaque ligne à la tabulation et les ajouter à la liste
                mots = line.split("\t")
                for mot in mots:
                    # Ajouter chaque mot en minuscule à la liste des capitales
                    capitales.append(mot.strip().lower())
                    
    except FileNotFoundError:
        print(f"Le fichier '{fileName}' n'a pas été trouvé.")
    
    return capitales

def build_dict(lst: list) -> dict:
    """
    Construit un dictionnaire où les clés sont les tailles des mots et les valeurs sont des listes
    de mots ayant cette taille.

    :param lst: Liste de mots
    :return: Dictionnaire des mots par taille
    """
    dictionnaire_mots = {}
    for mot in lst:
        taille = len(mot)
        #Si la taille n'est pas dans le dictionnaire on crée une nouvelle liste
        if taille not in dictionnaire_mots:
            dictionnaire_mots[taille] = []
        dictionnaire_mots[taille].append(mot)
    return dictionnaire_mots

def select_word(sorted_words: dict, word_len: int) -> str:
    """
    Sélectionne un mot au hasard dans la liste des mots de taille word_len du dictionnaire.

    :param sorted_words: Dictionnaire des mots par taille
    :param word_len: Longueur du mot souhaitée
    :return: Un mot aléatoire de la longueur spécifiée
    """
    if word_len in sorted_words:
        return random.choice(sorted_words[word_len])
    else:
        return ""  # Retourne une chaîne vide si aucune taille correspondante n'est trouvée

   
runGame()

