/**
 * Représente un personnage avec un nom, un âge, une position, et un propriétaire.
 * Cette classe est abstraite et est destinée à être étendue par des sous-classes spécifiques.
 */
abstract public class Personnage {

    /**
     * Le nom du personnage.
     */
    private String nom;

    /**
     * L'âge du personnage.
     */
    private int age;

    /**
     * La position actuelle du personnage.
     */
    private int position;

    /**
     * Le propriétaire du personnage, qui est un joueur.
     */
    private Joueur proprietaire;

    /**
     * Constructeur pour créer un personnage avec un nom et un âge.
     * 
     * @param nom le nom du personnage
     * @param age l'âge du personnage
     */
    public Personnage(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }

    /**
     * Déplace le personnage à une nouvelle position et attribue un gain de points au propriétaire.
     * 
     * @param destination la nouvelle position du personnage
     * @param gain le gain de points pour le propriétaire
     */
    public void deplacer(int destination, int gain) {
        this.position = destination;
        proprietaire.modifierPoints(gain);
    }

    /**
     * Applique une pénalité au propriétaire du personnage.
     * 
     * @param penalite le montant de la pénalité à soustraire des points du propriétaire
     */
    public void penaliser(int penalite) {
        proprietaire.modifierPoints(penalite);
    }

    /**
     * Retourne une représentation textuelle du personnage (son nom).
     * 
     * @return le nom du personnage
     */
    public String toString() {
        return nom;
    }

    /**
     * Méthode abstraite pour obtenir la position souhaitée du personnage.
     * Cette méthode doit être implémentée par les sous-classes.
     * 
     * @return la position souhaitée du personnage
     */
    public abstract int positionSouhaitee();

    /**
     * Retourne la position actuelle du personnage.
     * 
     * @return la position du personnage
     */
    public int getPosition() {
        return position;
    }

    /**
     * Modifie la position du personnage.
     * 
     * @param position la nouvelle position du personnage
     */
    public void setPosition(int position) {
        this.position = position;
    }

    /**
     * Retourne le nom du personnage.
     * 
     * @return le nom du personnage
     */
    public String getNom() {
        return nom;
    }

    /**
     * Retourne le propriétaire du personnage.
     * 
     * @return le propriétaire (un joueur) du personnage
     */
    public Joueur getProprietaire() {
        return this.proprietaire;
    }

    /**
     * Définit le propriétaire du personnage.
     * 
     * @param j le joueur qui devient le propriétaire du personnage
     */
    public void setProprietaire(Joueur j) {
        this.proprietaire = j;
    }
}
