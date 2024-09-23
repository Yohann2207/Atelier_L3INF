package question1;

import java.time.LocalDate;
import java.util.ArrayList;

/**
 * La classe Secretaire représente une secrétaire qui est un employé.
 * Elle peut être associée à plusieurs managers, jusqu'à un maximum de 5.
 * Elle hérite de la classe Employe.
 */
public class Secretaire extends Employe {

    /**
     * La liste des managers associés à la secrétaire.
     * Une secrétaire peut avoir jusqu'à 5 managers.
     */
    protected ArrayList<Manager> listeManager = new ArrayList<>();

    /**
     * Constructeur privé pour créer un objet Secretaire avec des informations personnelles,
     * un salaire, et une date d'embauche.
     *
     * @param nom      Le nom de la secrétaire.
     * @param prenom   Le prénom de la secrétaire.
     * @param date     La date de naissance de la secrétaire.
     * @param salaire  Le salaire de la secrétaire.
     * @param jE       Le jour d'embauche.
     * @param mE       Le mois d'embauche (0 pour janvier, 11 pour décembre).
     * @param aE       L'année d'embauche.
     */
    private Secretaire(String nom, String prenom, LocalDate date, double salaire, int jE, int mE, int aE) {
        super(nom, prenom, date, salaire, jE, mE, aE);
    }

    /**
     * Méthode statique pour créer un objet Secretaire si l'âge est compris entre 16 et 65 ans.
     * Sinon, renvoie {@code null}.
     *
     * @param nom      Le nom de la secrétaire.
     * @param prenom   Le prénom de la secrétaire.
     * @param date     La date de naissance de la secrétaire.
     * @param salaire  Le salaire de la secrétaire.
     * @param jE       Le jour d'embauche.
     * @param mE       Le mois d'embauche (0 pour janvier, 11 pour décembre).
     * @param aE       L'année d'embauche.
     * @return Un objet Secretaire si les critères sont respectés, sinon {@code null}.
     */
    public static Secretaire createSecretaire(String nom, String prenom, LocalDate date, double salaire, int jE, int mE, int aE) {
    	Personne temporaire= new Personne(nom, prenom, date); 
    	if ((temporaire.avoirAge()<16) || (temporaire.avoirAge()>65)){
    		return null;
        } else {
            return new Secretaire(nom, prenom, date, salaire, jE, mE, aE);
        }
    }

    /**
     * Associe un manager à la secrétaire, si le manager n'est pas déjà associé et 
     * si la secrétaire n'a pas plus de 5 managers.
     *
     * @param leManager Le manager à associer à la secrétaire.
     * @return {@code true} si le manager a été ajouté, sinon {@code false}.
     */
    public boolean setManager(Manager leManager) {
        boolean res = true;
        if (listeManager.contains(leManager) || listeManager.size() > 5) {
            res = false;
        } else {
            listeManager.add(leManager);
            leManager.setLaSecretaire(this);
        }
        return res;
    }

    /**
     * Affiche la liste des managers associés à la secrétaire.
     * Pour chaque manager, affiche son prénom.
     */
    public void afficheListManager() {
        for (Manager manager : listeManager) {
            System.out.println("Manager de " + getPrenom() + " : " + manager.getPrenom());
        }
    }

    /**
     * Supprime l'association entre la secrétaire et un manager donné.
     *
     * @param leManager Le manager à dissocier de la secrétaire.
     */
    public void deleteManager(Manager leManager) {
        if (listeManager.contains(leManager)) {
            leManager.deleteSecretaire(this);
        }
    }

    /**
     * Augmente le salaire de la secrétaire en fonction du nombre de managers associés.
     * Pour chaque manager, le salaire est augmenté de 0,1%.
     */
    public void augmenterLeSalaire() {
        if (listeManager.size() != 0) {
            for (int i = 0; i < listeManager.size(); i++) {
                this.augmenterLeSalaire(0.1);
            }
        }
    }
}
