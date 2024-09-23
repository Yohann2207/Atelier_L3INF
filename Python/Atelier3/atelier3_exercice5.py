def ouvrante(car: str) -> bool:
    """
    Vérifie si le caractère donné est une parenthèse, un crochet ou une accolade ouvrante.
    
    :param car: Le caractère à vérifier
    :return: True si le caractère est une parenthèse, un crochet ou une accolade ouvrante, False sinon
    """
    return car in '({['


def fermante(car: str) -> bool:
    """
    Vérifie si le caractère donné est une parenthèse, un crochet ou une accolade fermante.
    
    :param car: Le caractère à vérifier
    :return: True si le caractère est une parenthèse, un crochet ou une accolade fermante, False sinon
    """
    return car in ')}]'


def renverse(car: str) -> str:
    """
    Renvoie le caractère opposé pour les parenthèses, crochets et accolades.
    Si le caractère est un autre type (nombre, espace, opérateur, ou parenthèse ouvrante), il est renvoyé tel quel.
    
    :param car: Le caractère à vérifier
    :return: Le caractère opposé si c'est une parenthèse, un crochet ou une accolade fermante, sinon le caractère lui-même
    """
    correspondances = {
        ')': '(',
        ']': '[',
        '}': '{',
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    # Retourne le caractère correspondant si il est dans le dictionnaire, sinon retourne le caractère lui-même
    return correspondances.get(car, car)


def operateur(car: str) -> bool:
    """
    Vérifie si le caractère est un opérateur (+, *, -).
    
    :param car: Le caractère à vérifier
    :return: True si car est un opérateur (+, *, -), sinon False
    """
    return car in '+*-'


def nombre(car: str) -> bool:
    """
    Vérifie si la chaîne de caractères est un nombre (ne comporte que des chiffres).
    
    :param car: La chaîne de caractères à vérifier
    :return: True si car est un nombre, sinon False
    """
    return car.isdigit()


def caractere_valide(car: str) -> bool:
    """
    Vérifie si le caractère est valide dans une expression arithmétique.
    Un caractère est considéré valide s'il est une parenthèse, un crochet, une accolade,
    un chiffre, un opérateur ou un espace.

    :param car: Le caractère à vérifier
    :return: True si car est un caractère valide, sinon False
    """
    
    return(car == " " or operateur(car) or nombre(car) or ouvrante(car) or fermante(car))


def verif_parenthese(expression: str) -> bool:
    """
    Vérifie si l'expression arithmétique est valide et correctement parenthésée.
    
    :param expression: La chaîne de caractères représentant l'expression à vérifier
    :return: True si l'expression est valide et correctement parenthésée, False sinon
    """
    pile = []
    
    for car in expression:
        if not caractere_valide(car):
            return False
        if ouvrante(car):
            pile.append(car)
        elif fermante(car):
            if not pile or pile[-1] != renverse(car):
                return False
            pile.pop()
    
    return len(pile) == 0


print(verif_parenthese("(3+2) * 6-1"))   
print(verif_parenthese("((3+2)*6-1"))    
print(verif_parenthese("(5+7]*12"))
print(verif_parenthese("[(5+7)*12]"))