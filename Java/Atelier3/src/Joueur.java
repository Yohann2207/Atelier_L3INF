import java.util.ArrayList;

/**
 * Représente un joueur avec un nom, un code unique, un nombre de points,
 * et une liste de personnages associés. 
 * Le nombre total de joueurs est également suivi.
 */
public class Joueur {

    /**
     * Le nom du joueur.
     */
    private String nom;

    /**
     * Le code unique du joueur, généré automatiquement.
     */
    private String code;

    /**
     * Le nombre total de joueurs créés.
     */
    private static int nbJoueurs = 0;

    /**
     * Le nombre de points du joueur.
     */
    private int nbPoints;

    /**
     * La liste des personnages associés au joueur.
     */
    private ArrayList<Personnage> listePersos;

    /**
     * Constructeur pour créer un nouveau joueur.
     * Le code du joueur est généré automatiquement basé sur le nombre de joueurs.
     * Le joueur commence avec 0 points et une liste vide de personnages.
     * 
     * @param nom le nom du joueur
     */
    public Joueur(String nom) {
        this.nom = nom;
        nbJoueurs++;
        this.code = "J" + nbJoueurs;
        this.nbPoints = 0;
        this.listePersos = new ArrayList<>();
    }

    /**
     * Ajoute un personnage à la liste de personnages du joueur,
     * si le personnage n'a pas déjà de propriétaire.
     * 
     * @param p le personnage à ajouter
     */
    public void ajouterPersonnage(Personnage p) {
        if (p.getProprietaire() != null) {
            // Le personnage appartient déjà à un autre joueur, aucune action
        } else {
            this.listePersos.add(p);
            p.setProprietaire(this);
        }
    }

    /**
     * Modifie le nombre de points du joueur.
     * 
     * @param nb le nombre de points à ajouter (ou soustraire)
     */
    public void modifierPoints(int nb) {
        this.nbPoints += nb;
    }

    /**
     * Retourne le nombre de points du joueur.
     * 
     * @return le nombre de points
     */
    public int getPoints() {
        return nbPoints;
    }

    /**
     * Vérifie si le joueur peut jouer, c'est-à-dire s'il possède au moins
     * un personnage.
     * 
     * @return true si le joueur a des personnages, sinon false
     */
    public boolean peutJouer() {
        return !this.listePersos.isEmpty();
    }

    /**
     * Retourne une représentation en chaîne de caractères du joueur,
     * incluant son code, son nom, son nombre de points et le nombre
     * de personnages qu'il possède.
     * 
     * @return une chaîne représentant le joueur
     */
    public String toString() {
        String persoCount = (this.listePersos.size() == 0) ? "aucun personnage" :
            this.listePersos.size() + " personnage(s)";
        String points = (this.nbPoints == 1) ? "1 point" : this.nbPoints + " points";

        return this.code + " " + this.nom + " (" + points + ") avec " + persoCount;
    }

    /**
     * Retourne le nombre total de joueurs créés.
     * 
     * @return le nombre total de joueurs
     */
    public static int getNbJoueurs() {
        return nbJoueurs;
    }

    /**
     * Retourne la liste des personnages associés au joueur.
     * 
     * @return la liste des personnages du joueur
     */
    public ArrayList<Personnage> getListePerso() {
        return listePersos;
    }

    /**
     * Retourne le nom du joueur.
     * 
     * @return le nom du joueur
     */
    public String getNom() {
        return nom;
    }
}
