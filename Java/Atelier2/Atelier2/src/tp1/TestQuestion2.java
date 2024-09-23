package tp1;

import java.time.LocalDate;

import question1.Employe;
import question1.Manager;
import question1.Secretaire;

public class TestQuestion2 {

	public static void main(String[] args) {
		
		
		LocalDate date0 = LocalDate.of(2003, 07, 22);
		LocalDate date1 = LocalDate.of(1985, 12, 25);
		LocalDate date2 = LocalDate.of(2000, 1, 1);
		LocalDate date3 = LocalDate.of(1995, 3, 14);
		LocalDate date4 = LocalDate.of(2000, 7, 30);
		LocalDate date5 = LocalDate.of(2002, 10, 5);
		LocalDate date6 = LocalDate.of(1998, 6, 18);
		LocalDate date7 = LocalDate.of(1975, 9, 23);
		
		
		Employe e1  = Employe.createEmploye("fabbri", "yohann", date0, 2000.00, 21, 9, 2024);

		
		e1.augmenterLeSalaire(10);
		System.out.println(e1.getSalaire());
		System.out.println(e1.calculAnnuite() + " année(s) d'ancienneté");

		Manager m1 = Manager.createManager("Dupont", "Jean", date1, 3000.00, 22, 9, 2020);
		Manager m2 = Manager.createManager("Smith", "Alice", date2, 2800.00, 14, 7, 2021);
		Manager m3 = Manager.createManager("Doe", "John", date3, 3500.00, 1, 2, 2018);
		Manager m4 = Manager.createManager("Martin", "Lucie", date4, 3200.00, 10, 1, 2019);
		Manager m5 = Manager.createManager("Garcia", "Maria", date5, 4000.00, 25, 3, 2016);

		System.out.println(m1.toString());
		System.out.println(m1.getAnciennete() + " année(s) d'ancienneté");
		System.out.println("Salaire du manager : " + m1.getSalaire());

		Secretaire s1 = Secretaire.createSecretaire("Leroy", "Clara", date6, 3000.00, 5, 11, 2022);
		Secretaire s2 = Secretaire.createSecretaire("Smith", "Maria", date7, 3000.00, 5, 11, 2022);
		
		System.out.println(s1.toString());

		m1.setSecretaire(s1);
		m2.setSecretaire(s1);
		m3.setSecretaire(s1);
		m4.setSecretaire(s1);
		m5.setSecretaire(s1);
		s2.setManager(m2);
		
		s1.afficheListManager();
		s2.afficheListManager();

		s1.augmenterLeSalaire();
		System.out.println("Salaire de " + s1.getNom() + " : " + s1.getSalaire());

		s1.deleteManager(m1);

		System.out.println(m1.afficheSecretaire());
		
		s1.setManager(m1);
				
		System.out.println(m1.afficheSecretaire());

	}
}
