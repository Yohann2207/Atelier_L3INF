#Manon et Yohann

def est_bissextile(annee : int) -> bool: 
    """
    Détermine si une année est bissextile.

    Args:
        annee (int): L'année à vérifier.

    Returns:
        bool: True si l'année est bissextile, sinon False.
    """
    # Une année est bissextile si elle est divisible par 4
    # mais pas divisible par 100, sauf si elle est divisible par 400.
    return (((annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)))


# Exemple d'utilisation
def test():
    print(est_bissextile(2024))
    print(est_bissextile(2023))

test()

