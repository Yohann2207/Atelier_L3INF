package exercice5;

public class Vacataire extends Enseignant{
	
	
	protected static final double salaire_h = 40;
	protected int nbHeuresCours;
	
	
	protected Vacataire(String nom, int nbHeuresCours) {
		super(nom);
		this.nbHeuresCours = nbHeuresCours;
	}
	
	
	public double salaire() {
		return nbHeuresCours * salaire_h;
	}
	
	
	public String toString() {
        return nom + " (vacataire " + nbHeuresCours + " heures) : " + salaire() + " euros";
    }

}
