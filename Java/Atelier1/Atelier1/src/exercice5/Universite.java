package exercice5;

import java.util.ArrayList;

public class Universite {
	
	
	protected String nom;
	protected ArrayList<Enseignant> listeEnseignants = new ArrayList<>();
	
	
	protected Universite(String nom) {
		this.nom = nom;
	}
	
	
	protected void afficherSalaires() {
		 double totalSalaires = 0;
	     System.out.println("LISTE DES ENSEIGNANTS DE l'UNIVERSITE " + nom);
	     System.out.println("Effectif: " + listeEnseignants.size() + " enseignants");
	     for (Enseignant e : listeEnseignants) {
	         System.out.println(e.toString());
	         totalSalaires += e.salaire();
	     }
	     System.out.println("Total des salaires = " + totalSalaires + " euros");
	}
	
	
	protected void embaucher(Enseignant e) {
		listeEnseignants.add(e);
	}

}
