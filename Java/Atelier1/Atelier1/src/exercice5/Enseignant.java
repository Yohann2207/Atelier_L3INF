package exercice5;

public abstract class Enseignant {
	
	
	protected String nom;
	
	
	protected Enseignant(String nom) {
		this.nom = nom;
	}
	
	abstract public double salaire();
	
	
	public String getNom() {
		return nom;
	}
	
	public String toString() {
        return nom;
    }
}
