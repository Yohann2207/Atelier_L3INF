package question1;

import java.time.LocalDate;
import java.util.Calendar;
import java.util.GregorianCalendar;

/**
 * La classe Employe représente un employé qui hérite de la classe Personne.
 * Elle inclut des informations supplémentaires telles que le salaire et la date d'embauche.
 */
public class Employe extends Personne {
    
    /**
     * Le salaire de l'employé.
     */
    private double salaire;
    
    /**
     * La date d'embauche de l'employé représentée par un objet {@link GregorianCalendar}.
     */
    private final GregorianCalendar date_embauche;

    /**
     * Constructeur protégé pour créer un objet Employe avec des informations personnelles,
     * un salaire, et une date d'embauche.
     *
     * @param nom      Le nom de l'employé.
     * @param prenom   Le prénom de l'employé.
     * @param date     La date de naissance de l'employé.
     * @param salaire  Le salaire de l'employé.
     * @param jE       Le jour de l'embauche.
     * @param mE       Le mois de l'embauche (0 pour janvier, 11 pour décembre).
     * @param aE       L'année de l'embauche.
     */
    protected Employe(String nom, String prenom, LocalDate date, double salaire, int jE, int mE, int aE) {
        super(nom, prenom, date);
        this.salaire = salaire;
        this.date_embauche = new GregorianCalendar(aE, mE, jE);
    }

    /**
     * Méthode statique pour créer un objet Employe avec des validations sur l'âge.
     * Si l'âge est inférieur à 16 ans ou supérieur à 65 ans, l'employé ne peut pas être créé.
     *
     * @param nom      Le nom de l'employé.
     * @param prenom   Le prénom de l'employé.
     * @param date     La date de naissance de l'employé.
     * @param salaire  Le salaire de l'employé.
     * @param jE       Le jour de l'embauche.
     * @param mE       Le mois de l'embauche (0 pour janvier, 11 pour décembre).
     * @param aE       L'année de l'embauche.
     * @return Un objet Employe si les critères d'âge sont respectés, sinon {@code null}.
     */
    public static Employe createEmploye(String nom, String prenom, LocalDate date, double salaire, int jE, int mE, int aE) {
    	Personne temporaire= new Personne(nom, prenom, date); 
    	if ((temporaire.avoirAge()<16) || (temporaire.avoirAge()>65)) {
            return null;
        } else {
            return new Employe(nom, prenom, date, salaire, jE, mE, aE);
        }
    }

    /**
     * Renvoie le salaire de l'employé.
     *
     * @return Le salaire actuel de l'employé.
     */
    public double getSalaire() {
        return salaire;
    }

    /**
     * Modifie le salaire de l'employé.
     *
     * @param salaire Le nouveau salaire de l'employé.
     */
    public void setSalaire(double salaire) {
        this.salaire = salaire;
    }

    /**
     * Augmente le salaire de l'employé d'un certain pourcentage.
     *
     * @param pourcentage Le pourcentage d'augmentation du salaire.
     */
    public void augmenterLeSalaire(double pourcentage) {
        if (pourcentage > 0) {
            double augmentation = (salaire / 100) * pourcentage;
            salaire += augmentation;
        }
    }

    /**
     * Calcule l'ancienneté (en années) de l'employé en fonction de sa date d'embauche.
     *
     * @return Le nombre d'années d'ancienneté de l'employé.
     */
    public int calculAnnuite() {
        Calendar date_ajd = new GregorianCalendar();
        int annee = date_ajd.get(Calendar.YEAR) - date_embauche.get(Calendar.YEAR);
        int mois = date_ajd.get(Calendar.MONTH) + 1 - date_embauche.get(Calendar.MONTH);
        int jours = date_ajd.get(Calendar.DAY_OF_MONTH) - date_embauche.get(Calendar.DAY_OF_MONTH);

        // Si l'année en cours est supérieure à l'année d'embauche, on compte l'année même si elle est partielle
        if (mois > 0 || (mois == 0 && jours >= 0)) {
            annee++;  // Année commencée, donc on l'ajoute
        }
        return annee;
    }

}
