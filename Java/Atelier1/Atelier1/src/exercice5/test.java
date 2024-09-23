package exercice5;

public class test {

	public static void main(String[] args) {
		Universite universite = new Universite("Pascal Paoli");

        Titulaire titulaire1 = new Titulaire("Pierre", 1500.0);
        Titulaire titulaire2 = new Titulaire("Laurent", 2500.0);
        Vacataire vacataire1 = new Vacataire("Michel", 15);
        Vacataire vacataire2 = new Vacataire("Marie", 60);

        universite.embaucher(titulaire1);
        universite.embaucher(titulaire2);
        universite.embaucher(vacataire1);
        universite.embaucher(vacataire2);

        universite.afficherSalaires();
	}

}
