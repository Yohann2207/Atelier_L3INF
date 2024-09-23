package exCH4_2;

//exercice 4.4
public class TestPersonne2 {
	//Classes Personne, Etudiant, Enseignant de l'exercice 4.2
	public static void main(String[] args) {		
		Personne p1=new Personne("Marie",20);
		
		Personne p2=new Etudiant("Machin",26,"20202134");
		
		Personne p3=new Enseignant("Toto",34,2000,192);
		
		Etudiant p4=new Etudiant("Jean", 21,"20203433");
		
		Personne p5= new Enseignant("Pierre",54,3000,250);
		
		p1=p4;//upcast OK
		p1= p5;	
		
		p4= (Etudiant) p2;
		//p4= (Etudiant)p2;//tentative de downcast d'une personne en etudiant
		//ajout d'un cast explicite
		p5=p1;
		p5=p4;//upcast Ok	
		
		((Etudiant)p2).setNumEtu("20205784");
		//((Etudiant)p2).setNumEtu("20205784");//méthode setNumEtu illégale sur le type Personne
		
		p4.setNumEtu("20205785");
		
		((Etudiant)p5).setNumEtu("20205786");
		//méthode setNumEtu illégale sur le type Personne
		//Un cast explicite passe à la compilation mais
		//ilo provoquera une erreur à l'exécution
		
	}

}
