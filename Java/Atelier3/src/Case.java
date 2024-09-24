/**
 * Représente une case dans un jeu, qui peut contenir un personnage, un obstacle,
 * et être associée à un gain. Une case peut être libre ou occupée.
 */
public class Case {

    /**
     * Le gain de points associé à la case.
     */
    private int gain;

    /**
     * Le personnage qui occupe éventuellement la case.
     */
    private Personnage perso;

    /**
     * L'obstacle qui occupe éventuellement la case.
     */
    private Obstacle obs;

    /**
     * Constructeur pour créer une case avec un obstacle et un gain.
     * 
     * @param obs l'obstacle sur la case
     * @param gain le gain de points associé à la case
     */
    protected Case(Obstacle obs, int gain) {
        this.obs = obs;
        this.gain = gain;
    }

    /**
     * Constructeur pour créer une case sans obstacle, uniquement avec un gain.
     * 
     * @param gain le gain de points associé à la case
     */
    protected Case(int gain) {
        this(null, gain);
    }

    /**
     * Retourne la pénalité de l'obstacle sur la case.
     * Si aucun obstacle n'est présent, la pénalité est de 0.
     * 
     * @return la pénalité de l'obstacle ou 0 si la case est sans obstacle
     */
    public int getPenalite() {
        if (this.obs == null) {
            return 0;
        }
        return obs.getPenalite();
    }

    /**
     * Place un personnage sur la case.
     * 
     * @param perso le personnage à placer sur la case
     */
    public void placerPersonnage(Personnage perso) {
        this.perso = perso;
    }

    /**
     * Place un obstacle sur la case.
     * 
     * @param obs l'obstacle à placer sur la case
     */
    public void placerObstacle(Obstacle obs) {
        this.obs = obs;
    }

    /**
     * Enlève le personnage de la case.
     */
    public void enleverPersonnage() {
        this.perso = null;
    }

    /**
     * Vérifie si la case est libre, c'est-à-dire sans personnage et sans obstacle.
     * 
     * @return true si la case est libre, sinon false
     */
    public boolean estLibre() {
        return (this.obs == null) && (this.perso == null);
    }

    /**
     * Vérifie si la case est sans obstacle.
     * 
     * @return true si la case n'a pas d'obstacle, sinon false
     */
    public boolean sansObstacle() {
        return this.obs == null;
    }

    /**
     * Vérifie si la case est sans personnage.
     * 
     * @return true si la case n'a pas de personnage, sinon false
     */
    public boolean sansPerso() {
        return this.perso == null;
    }

    /**
     * Retourne le gain de points associé à la case.
     * 
     * @return le gain de la case
     */
    public int getGain() {
        return gain;
    }

    /**
     * Retourne une représentation textuelle de la case, indiquant si elle est
     * libre, si elle contient un obstacle, ou un personnage avec les informations
     * sur le gain ou la pénalité associée.
     * 
     * @return une chaîne représentant l'état de la case
     */
    public String toString() {
        if (estLibre()) {
            return "Libre (gain = " + getGain() + ")";
        }
        if (!sansObstacle()) {
            return "Obstacle (penalite = " + getPenalite() + ")";
        } else {
            return perso.toString() + " (penalite = -" + getGain() + ")";
        }
    }

    /**
     * Définit un nouvel obstacle sur la case.
     * 
     * @param obstacle l'obstacle à placer sur la case
     */
    public void setObstacle(Obstacle obstacle) {
        this.obs = obstacle;
    }

    /**
     * Retourne le personnage actuellement sur la case.
     * 
     * @return le personnage sur la case ou null si aucun personnage n'est présent
     */
    public Personnage getPersonnage() {
        return perso;
    }

    /**
     * Retourne l'obstacle actuellement sur la case.
     * 
     * @return l'obstacle sur la case ou null si aucun obstacle n'est présent
     */
    public Obstacle getObstacle() {
        return obs;
    }
}
