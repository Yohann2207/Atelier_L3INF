lettre : str = input("Quel type de lettre voulez-vous envoyer : ")
poids : int = int(input("Quel poids fait votre lettre (en grammes) : "))

# Verification du type de lettre et du calcul du prix selon les plages de poids
if lettre == "verte":
    if poids <= 20:
        prix = 1.16
    elif 20 < poids <= 100:
        prix = 2.32
    elif 100 < poids <= 250:
        prix = 4.00
    elif 250 < poids <= 500:
        prix = 6.00
    elif 500 < poids <= 1000:
        prix = 7.50
    elif 1000 < poids <= 3000:
        prix = 10.50

elif lettre == "prioritaire":
    if poids <= 20:
        prix = 1.43
    elif 20 < poids <= 100:
        prix = 2.86
    elif 100 < poids <= 250:
        prix = 5.26
    elif 250 < poids <= 500:
        prix = 7.89
    elif 500 < poids <= 3000:
        prix = 11.44

elif lettre == "ecopli":
    if poids <= 20:
        prix = 1.14
    elif 20 < poids <= 100:
        prix = 2.28
    elif 100 < poids <= 250:
        prix = 3.92

elif lettre == "outre-mer":
    if poids <= 500:
        prix = 8.35
    elif 500 < poids <= 1000:
        prix = 11.20
    elif 1000 < poids <= 2000:
        prix = 14.10
    elif 2000 < poids <= 5000:
        prix = 23.65
    elif 5000 < poids <= 10000:
        prix = 37.50
    elif 10000 < poids <= 15000:
        prix = 75.85
    elif 15000 < poids <= 30000:
        prix = 87.40

elif lettre == "cecogramme":
    prix = 0

#option pour sticker suivi
ajout_supplement = 0
if lettre in ["verte", "prioritaire", "ecopli"]:
    supplement = input("Souhaitez-vous ajouter un sticker suivi pour 0.50 € (oui/non) : ")
    if supplement == "oui":
        ajout_supplement = 0.50

prix_total = prix + ajout_supplement
print(f"Votre prix sera de {prix_total} €")


