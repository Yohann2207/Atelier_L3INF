package question1;

import java.time.LocalDate;

/**
 * La classe Manager représente un employé avec un poste de manager, qui peut avoir une secrétaire
 * associée et dont le salaire augmente en fonction de l'ancienneté.
 * Elle hérite de la classe Employe.
 */
public class Manager extends Employe {
    
    /**
     * La secrétaire associée au manager.
     */
    private Secretaire laSecretaire = null;
    
    /**
     * L'ancienneté du manager calculée en années.
     */
    private final int anciennete;

    /**
     * Constructeur privé pour créer un objet Manager avec des informations personnelles,
     * un salaire, et une date d'embauche. L'ancienneté est calculée à partir de la date d'embauche.
     * Le salaire est augmenté en fonction de l'ancienneté.
     *
     * @param nom      Le nom du manager.
     * @param prenom   Le prénom du manager.
     * @param date     La date de naissance du manager.
     * @param salaire  Le salaire du manager.
     * @param jE       Le jour d'embauche.
     * @param mE       Le mois d'embauche (0 pour janvier, 11 pour décembre).
     * @param aE       L'année d'embauche.
     */
    private Manager(String nom, String prenom, LocalDate date, double salaire, int jE, int mE, int aE) {
        super(nom, prenom, date, salaire, jE, mE, aE);
        anciennete = this.calculAnnuite();
        augmenterLeSalaire();
    }

    /**
     * Méthode statique pour créer un objet Manager si l'âge est compris entre 16 et 65 ans.
     * Sinon, renvoie {@code null}.
     *
     * @param nom      Le nom du manager.
     * @param prenom   Le prénom du manager.
     * @param date     La date de naissance du manager.
     * @param salaire  Le salaire du manager.
     * @param jE       Le jour d'embauche.
     * @param mE       Le mois d'embauche (0 pour janvier, 11 pour décembre).
     * @param aE       L'année d'embauche.
     * @return Un objet Manager si les critères sont respectés, sinon {@code null}.
     */
    public static Manager createManager(String nom, String prenom, LocalDate date, double salaire, int jE, int mE, int aE) {
    	Personne temporaire= new Personne(nom, prenom, date); 
    	if ((temporaire.avoirAge()<16) || (temporaire.avoirAge()>65)){
    		return null;
        } else {
            return new Manager(nom, prenom, date, salaire, jE, mE, aE);
        }
    }

    /**
     * Augmente le salaire du manager en fonction de son ancienneté.
     * Pour chaque année d'ancienneté, le salaire est augmenté de 0,5%.
     */
    protected void augmenterLeSalaire() {
        if (anciennete != 0) {
            for (int i = 0; i < anciennete; i++) {
                this.augmenterLeSalaire(0.5);
            }
        }
    }

    /**
     * Définit la secrétaire associée au manager. Si le manager n'a pas encore de secrétaire,
     * et que la secrétaire accepte le manager, elle est assignée au manager.
     *
     * @param uneSecretaire La secrétaire à assigner au manager.
     */
    public void setSecretaire(Secretaire uneSecretaire) {
        if (laSecretaire != uneSecretaire) {
            if (uneSecretaire.setManager(this)) {
                laSecretaire = uneSecretaire;
                System.out.println("Ajout de la secrétaire");
            }
        }
    }

    /**
     * Supprime l'association entre le manager et sa secrétaire.
     *
     * @param uneSecretaire La secrétaire à retirer du manager.
     */
    protected void deleteSecretaire(Secretaire uneSecretaire) {
        if (uneSecretaire.listeManager.contains(this)) {
            laSecretaire = null;
            uneSecretaire.listeManager.remove(this);
        }
    }

    /**
     * Affiche le prénom et le nom de la secrétaire associée au manager.
     * Si aucune secrétaire n'est associée, renvoie un message indiquant l'absence de secrétaire.
     *
     * @return Une chaîne de caractères avec le nom de la secrétaire ou un message d'absence.
     */
    public String afficheSecretaire() {
        String message = "La secrétaire n'est pas définie";
        if (laSecretaire != null) {
            message = "La secrétaire de " + getPrenom() + " est : " + laSecretaire.getPrenom() + " " + laSecretaire.getNom();
        }
        return message;
    }

    /**
     * Renvoie l'ancienneté du manager en années.
     *
     * @return L'ancienneté du manager.
     */
    public int getAnciennete() {
        return anciennete;
    }

    /**
     * Renvoie la secrétaire associée au manager.
     *
     * @return La secrétaire du manager, ou {@code null} si aucune secrétaire n'est associée.
     */
    public Secretaire getLaSecretaire() {
        return laSecretaire;
    }

    /**
     * Définit la secrétaire associée au manager.
     *
     * @param laSecretaire La nouvelle secrétaire à assigner au manager.
     */
    public void setLaSecretaire(Secretaire laSecretaire) {
        this.laSecretaire = laSecretaire;
    }
}
