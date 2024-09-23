package exercice4;

public class TestPersonne {

	public static void main(String[] args) {
		
		Personne pers = new Personne("Marie", 20);
		pers.afficher();
		
		Etudiant etu = new Etudiant();
		etu.afficher();
		etu.setNom("Pierre");
		etu.setAge(21);
		etu.setNumEtu("20203456");
		etu.afficher();
		
	}
}
