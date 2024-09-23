package exercice4;

public class Etudiant extends Personne{
	
	private String numEtu;
	
	
	protected Etudiant() {
		
	}
	
	protected Etudiant(String nom, int age, String numEtu) {
		super(nom, age);
		this.numEtu = numEtu;
	}
	
	protected void setNumEtu(String numEtu) {
		this.numEtu = numEtu;
	}
	
	public String toString() {
		return "Etudiant numero " + this.numEtu + " " + super.toString();
	}
	
	public void afficher() {
		System.out.println("*******Etudiant*******\n" + "Numero étudiant : 20203433");
		super.afficher();
	}

}
