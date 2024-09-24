/**
 * Représente un personnage de type Tauren, caractérisé par son nom, son âge et sa taille.
 * Le Tauren a une méthode spécifique pour déterminer la position souhaitée.
 */
public class Tauren extends Personnage {

    /**
     * La taille du Tauren, utilisée pour déterminer sa position souhaitée.
     */
    private int taille;

    /**
     * Constructeur pour créer un Tauren avec un nom, un âge et une taille.
     * 
     * @param nom le nom du Tauren
     * @param age l'âge du Tauren
     * @param taille la taille du Tauren
     */
    protected Tauren(String nom, int age, int taille) {
        super(nom, age);
        this.taille = taille;
    }

    /**
     * Calcule et retourne la position souhaitée par le Tauren, basée sur sa taille et 
     * sa position actuelle. La position souhaitée est une valeur aléatoire ajoutée à 
     * la position actuelle.
     * 
     * @return la position souhaitée par le Tauren
     */
    public int positionSouhaitee() {
        return (int) ((this.getPosition() + Math.random() * taille) + 1);
    }

    /**
     * Retourne une représentation textuelle du Tauren, incluant son type et son nom.
     * 
     * @return une chaîne représentant le Tauren
     */
    public String toString() {
        return "Tauren " + this.getNom();
    }
}
