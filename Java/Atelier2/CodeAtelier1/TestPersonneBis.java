public class TestPersonneBis {
	public static void main(String[] args) {		
		Personne pers=new Personne("Marie",20);
		Etudiant etu=new Etudiant("Jean", 21,"20203433");
		Enseignant ens= new Enseignant("Pierre",54,3000,250);
		System.out.println(pers);
		System.out.println(etu);
		System.out.println(ens);
		pers.afficher();
		etu.afficher();
		ens.afficher();
		}

}
