package question1;

import java.time.LocalDate;
import java.time.Month;

/**
 * La classe Personne représente une personne avec un nom, un prénom et une date de naissance.
 * Elle permet de manipuler et comparer des personnes en fonction de leurs informations personnelles.
 */
public class Personne {
    
    /**
     * Le nom de la personne.
     */
    protected String nom;
    
    /**
     * Le prénom de la personne.
     */
    protected String prenom;
    
    /**
     * La date de naissance de la personne sous forme de chaîne de caractères.
     */
    protected LocalDate date;
    
    /**
     * Le nombre total de personnes créées.
     */
    static int nb_personnes = 0;

    /**
     * Constructeur qui initialise une personne avec un nom et un âge.
     * Le nombre total de personnes est incrémenté.
     *
     * @param nom Le nom de la personne.
     */
    public Personne(String nom) {
        this.nom = nom;
        nb_personnes += 1;
    }

    /**
     * Constructeur par défaut qui initialise une personne avec des valeurs par défaut.
     * Le nombre total de personnes est incrémenté.
     */
    public Personne() {
        this("");
        nb_personnes += 1;
    }

    /**
     * Constructeur qui initialise une personne avec un nom, un prénom et une date de naissance.
     * Le nombre total de personnes est incrémenté.
     *
     * @param nom Le nom de la personne.
     * @param prenom Le prénom de la personne.
     * @param date La date de naissance de la personne.
     */
    public Personne(String nom, String prenom, LocalDate date) {
        this.nom = nom;
        this.prenom = prenom;
        this.date = date;
        nb_personnes += 1;
    }

    /**
     * Définit le nom de la personne.
     *
     * @param nom Le nom de la personne.
     */
    public void setNom(String nom) {
        this.nom = nom;
    }

    /**
     * Renvoie le nom de la personne.
     *
     * @return Le nom de la personne.
     */
    public String getNom() {
        return nom;
    }
    
    public LocalDate getDate() {
        return date;
    }

    /**
     * Renvoie le prénom de la personne.
     *
     * @return Le prénom de la personne.
     */
    public String getPrenom() {
        return prenom;
    }

    /**
     * Affiche le nom de la personne.
     */
    public void afficher() {
        System.out.println("Nom : " + this.nom);
    }

    /**
     * Renvoie une représentation sous forme de chaîne de caractères de la personne.
     *
     * @return Une chaîne de caractères contenant le nom de la personne.
     */
    public String toString() {
        return this.nom;
    }

    /**
     * Compare l'âge de deux personnes et renvoie si la première est plus âgée que la seconde.
     *
     * @param p1 La première personne.
     * @param p2 La seconde personne.
     * @return {@code true} si p1 est plus âgée que p2, sinon {@code false}.
     */
    public static boolean plusAgee(Personne p1, Personne p2) {
        return (p1.avoirAge() > p2.avoirAge());
    }

    /**
     * Compare l'âge de cette personne avec une autre personne et renvoie si cette personne est plus âgée.
     *
     * @param p L'autre personne à comparer.
     * @return {@code true} si cette personne est plus âgée que p, sinon {@code false}.
     */
    public boolean plusAgee(Personne p) {
        return (this.avoirAge() > p.avoirAge());
    }
    
    /**
     * Retourne l'age de la personne
     * 
     * @return 
     */
    public int avoirAge() {
        LocalDate date_mtn = LocalDate.now();
        int annee = date_mtn.getYear();
        Month mois = date_mtn.getMonth(); 
        int jour = date_mtn.getDayOfMonth();

        LocalDate date_anniv=this.getDate();
        int annee_anniv = date_anniv.getYear();
        Month mois_anniv = date_anniv.getMonth(); 
        int jour_anniv = date_anniv.getDayOfMonth();

        if ((mois.ordinal()>=mois_anniv.ordinal())&&(jour>=jour_anniv)) {
            return(annee-annee_anniv); 
        }
        else {
            return(annee-annee_anniv-1);
        }
    }

    /**
     * Vérifie si cette personne est égale à une autre personne en comparant le nom, le prénom et la date de naissance.
     *
     * @param p2 L'autre personne à comparer.
     * @return {@code true} si les deux personnes sont identiques, sinon {@code false}.
     */
    public boolean egalite(Personne p2) {
        String nom1 = this.nom;
        String prenom1 = this.prenom;
        String date1 = this.date.toString();
        String nom2 = p2.nom;
        String prenom2 = p2.prenom;
        String date2 = p2.date.toString();
        return (nom1.equals(nom2) && prenom1.equals(prenom2) && date1.equals(date2));
    }
}
