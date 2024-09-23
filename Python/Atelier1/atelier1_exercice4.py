#Manon et Yohann

from datetime import date

def est_bissextile(annee):
    """Détermine si une année est bissextile."""
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def date_est_valide(jour, mois, annee):
    """Vérifie si une date est valide.

    Args:
        jour (int): Le jour de la date.
        mois (int): Le mois de la date.
        annee (int): L'année de la date.

    Returns:
        bool: True si la date est valide, sinon False.
    """
    
    if annee < 1:
        return False

    
    if mois < 1 or mois > 12:
        return False

    # Nombre de jours par mois
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Ajuster pour février si l'année est bissextile
    if mois == 2 and est_bissextile(annee):
        jours_par_mois[1] = 29

    # Vérifier si le jour est valide pour le mois donné
    return 1 <= jour and jour <= jours_par_mois[mois - 1]

print(date_est_valide(29,2,2024))
print(date_est_valide(34,2,2024))
print(date_est_valide(22,7,2003))

def saisie_date_naissance():
    jour = int(input("Donnez votre jour de naissance : "))
    mois = int(input("Donnez votre mois de naissance : "))
    annee = int(input("Donnez votre annee de naissance : "))
    return date(annee,mois,jour)

"""
print(saisie_date_naissance())
"""

def age(date_naissance) -> int:
    annee_de_naissance = date_naissance.year
    aujourdhui = date.today()
    annee_en_cours = aujourdhui.year
    age = annee_en_cours - annee_de_naissance
    if date_naissance.month >= aujourdhui.month and date_naissance.day > aujourdhui.day:
        age = age - 1
    return age

print(age(date(2003,9,5)))
print(age(date(2003,7,22)))

def est_majeur(date_naissance) -> bool:
    return age(date_naissance) >= 18

print(est_majeur(date(2009,7,22)))
print(est_majeur(date(2003,7,22)))

def test_acces():
    date_naissance = saisie_date_naissance()
    verif_age = str(age(date_naissance))
    if est_majeur(date_naissance):
        print("Bonjour vous avez " + verif_age + " ans, accès autorisé")
    else:
        print("Désolé, vous avez " + verif_age + " ans, accès interdit")

test_acces()


