package exercice4;

public class Enseignant extends Personne{
	
	private double salaire;
	private double nbheuresCours;
	
	protected Enseignant(String nom, int age, double salaire, double nbheuresCours) {
		super(nom, age);
		this.salaire = salaire;
		this.nbheuresCours = nbheuresCours;
	}
	
	public String toString() {
		return "Enseignant " + super.toString() + " " + this.salaire;
	}
	
	public void afficher() {
		System.out.println("*******Enseignant******");
		super.afficher();
		System.out.println("Salaire : " + this.salaire + "\nNombre d'heures de cours : " + this.nbheuresCours);
	}

}
