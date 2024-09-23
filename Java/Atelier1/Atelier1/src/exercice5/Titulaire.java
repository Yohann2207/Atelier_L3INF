package exercice5;

public class Titulaire extends Enseignant{
	
	
	protected double salaire;
	
	
	protected Titulaire(String nom, double salaire) {
		super(nom);
		this.salaire = salaire;
	}
	
	
	public double salaire() {
		return salaire;
	}
	
	
	public String toString() {
        return nom + " (titulaire)  : " + salaire() + " euros";
    }

}
