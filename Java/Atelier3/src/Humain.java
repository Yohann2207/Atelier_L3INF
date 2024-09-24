/**
 * Représente un personnage de type Humain, avec un niveau et un compteur de déplacements.
 * Le niveau du Humain peut augmenter en fonction du nombre de déplacements effectués.
 */
public class Humain extends Personnage {

    /**
     * Le nombre total de déplacements effectués par tous les personnages Humain.
     */
    private static int nbDeplacements = 0;

    /**
     * Le niveau du Humain, qui peut augmenter après un certain nombre de déplacements.
     */
    private int niveau;

    /**
     * Constructeur pour créer un Humain avec un nom et un âge.
     * Le niveau initial du Humain est fixé à 1.
     * 
     * @param nom le nom du Humain
     * @param age l'âge du Humain
     */
    protected Humain(String nom, int age) {
        super(nom, age);
        this.niveau = 1;
    }

    /**
     * Déplace le Humain à une nouvelle destination, modifie les points du propriétaire,
     * et met à jour le compteur de déplacements. Le niveau du Humain augmente après 
     * 4 et 6 déplacements.
     * 
     * @param destination la nouvelle position du Humain
     * @param gain le gain de points pour le propriétaire
     */
    public void deplacer(int destination, int gain) {
        super.deplacer(destination, gain);
        nbDeplacements += 1;
        if (nbDeplacements == 4) {
            setNiveau(2);
        }
        if (nbDeplacements == 6) {
            setNiveau(3);
        }
    }

    /**
     * Modifie le niveau du Humain.
     * 
     * @param niveau le nouveau niveau du Humain
     */
    public void setNiveau(int niveau) {
        this.niveau = niveau;
    }

    /**
     * Retourne le niveau actuel du Humain.
     * 
     * @return le niveau du Humain
     */
    public int getNiveau() {
        return niveau;
    }

    /**
     * Calcule et retourne la position souhaitée par le Humain.
     * La position souhaitée est basée sur la position actuelle, le niveau, et le nombre de déplacements.
     * 
     * @return la position souhaitée par le Humain
     */
    public int positionSouhaitee() {
        return (int) ((this.getPosition() + this.getNiveau()) * nbDeplacements);
    }

    /**
     * Retourne une représentation textuelle du Humain, incluant son type et son nom.
     * 
     * @return une chaîne représentant le Humain
     */
    public String toString() {
        return "Humain " + this.getNom();
    }
}
