def full_name(strNomprenom: str) -> str:
    """
    Transforme une chaîne de type 'nom prenom' en une chaîne avec le nom en majuscules
    et le prénom avec seulement la première lettre en majuscule.

    Paramètres:
    strNomprenom (str): Une chaîne de caractères contenant le nom et le prénom séparés par un espace.

    Retourne:
    str: La chaîne formatée avec le nom en majuscules et le prénom avec la première lettre en majuscule.

    Exceptions:
    ValueError: Si le format de l'entrée est invalide (pas exactement deux parties).
    """
    try:
        #Séparer la chaîne de caractères en nom et prénom
        parties = strNomprenom.split()

        #Vérifier qu'il y a bien deux parties
        if len(parties) != 2:
            raise ValueError("Format invalide. Veuillez entrer 'nom prenom'.")

        nom, prenom = parties
        # Mettre le nom en majuscules et le prénom avec seulement la première lettre en majuscule
        return f"{nom.upper()} {prenom.capitalize()}"
    
    except ValueError as e:
        # Afficher le message d'erreur et le retourner
        print(e)


print(full_name("bisgambiglia paul")) 
print(full_name("martin jean pierre"))  
print(full_name(""))  


def is_mail(strMail: str) -> tuple:
    """
    Vérifie la validité d'une adresse e-mail et renvoie un tuple indiquant la validité et un code d'erreur.

    Paramètres:
    str_arg (str): Une chaîne de caractères représentant une adresse e-mail.

    Retourne:
    tuple: Un tuple composé de (validité, code d'erreur)
                - (1, x): Le mail est valide.
                - (0, 1): Le mail n'est pas valide, le corps n'est pas valide.
                - (0, 2): Le mail n'est pas valide, il manque l'@.
                - (0, 3): Le mail n'est pas valide, le domaine n'est pas valide.
                - (0, 4): Le mail n'est pas valide, il manque le '.'.
    """
    validité = 1
    code_erreur = 0

    # Vérifier si l'adresse contient un '@'
    if '@' not in strMail:
        validité = 0
        code_erreur = 2
    else:
        # Séparer l'adresse en corps et domaine
        corps, domaine = strMail.split('@')

        # Vérifier la validité du corps
        if not corps or corps.startswith('.') or corps.endswith('.') or '..' in corps:
            validité = 0
            code_erreur = 5
        # Vérifier la validité du domaine
        elif not domaine or domaine.startswith('.') or domaine.endswith('.') or '..' in domaine:
            validité = 0
            code_erreur = 3
        # Vérifier si le domaine contient un '.'
        elif '.' not in domaine:
            validité = 0
            code_erreur = 4

    return validité, code_erreur

# Programme de test pour afficher le type d'erreur
def test_is_mail(email: str) -> str:
    validité, code_erreur = is_mail(email)
    
    messages = {
        2: "Le mail n'est pas valide, il manque l'@.",
        3: "Le mail n'est pas valide, le domaine n'est pas valide.",
        4: "Le mail n'est pas valide, il manque le '.'.",
        5: "Le mail n'est pas valide, le corps n'est pas valide."
    }
    
    if validité == 1:
        print(f"{email} -> Le mail est valide.")
    else:
        print(f"{email} -> ",  messages[code_erreur])

test_is_mail('bisgambiglia_paul@univ-corse.fr')       
test_is_mail('bisgambiglia_paulOuniv-corse.fr')
test_is_mail('bisgambiglia_paul@univ-corse..fr')       
test_is_mail('bisgambiglia_paul@univ-corsePOINTfr')   
test_is_mail('@univ-corse.fr')
test_is_mail('')                                       

