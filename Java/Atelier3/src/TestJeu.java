
public class TestJeu {
	
	public static void main(String[] args) {
		
		 	Jeu jeu = new Jeu("Atelier POO", 4, 10);
		 	
	        Joueur j1 = new Joueur("Paul"); 
	        Tauren t1 = new Tauren("Hector", 15, 10); 
	        Humain h1 = new Humain("Jean", 10); 

	        j1.ajouterPersonnage(t1);
	        j1.ajouterPersonnage(h1);
	        jeu.ajouterJoueur(j1);
	        
	        Joueur j2 = new Joueur("Lucien"); 
	        Tauren t2 = new Tauren("Hercule", 20, 5); 
	        Humain h2 = new Humain("Marie", 10); 
	        
	        j2.ajouterPersonnage(t2);
	        j2.ajouterPersonnage(h2);
	        jeu.ajouterJoueur(j2);

	        
	        jeu.lancerJeu();
		
	}
}


