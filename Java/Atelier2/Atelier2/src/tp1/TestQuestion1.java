package tp1;

import java.time.LocalDate;

import question1.Personne;

public class TestQuestion1 {

	public static void main(String[] args) {
			
			
			LocalDate date1 = LocalDate.of(1990, 5, 15);
			LocalDate date2 = LocalDate.of(1991, 5, 15);
			LocalDate date3 = LocalDate.of(1990, 5, 15);
			 
			
			Personne p1 = new Personne("Fabbri", "Yohann", date1); 
			Personne p2 = new Personne("Mars", "Manon", date2);
			Personne p3 = new Personne("Fabbri", "Yohann", date3);  
			System.out.println(Personne.plusAgee(p1,p2));
			System.out.println(Personne.plusAgee(p2,p1));
			System.out.println(p1.plusAgee(p2));
			System.out.println(p2.plusAgee(p1));
			System.out.println(p1.egalite(p2));
			System.out.println(p1.egalite(p3));
		}
}
