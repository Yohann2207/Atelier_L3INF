/**
 * Représente un obstacle qui a une pénalité associée.
 */
public class Obstacle {

    /**
     * La pénalité associée à l'obstacle.
     */
    private int penalite;

    /**
     * Constructeur de la classe Obstacle.
     * 
     * @param penalite la valeur de la pénalité associée à cet obstacle
     */
    public Obstacle(int penalite) {
        this.penalite = penalite;
    }

    /**
     * Retourne la pénalité associée à cet obstacle.
     * 
     * @return la valeur de la pénalité
     */
    public int getPenalite() {
        return penalite;
    }
}
