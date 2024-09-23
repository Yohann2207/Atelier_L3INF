package exercice3;

import java.text.DecimalFormat;

public class testAPI {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DecimalFormat df = new DecimalFormat("#0.00"); 
		System.out.println(df.format(Math.PI));
		System.out.println(df.format(Math.random()));
		int x = (int)(Math.random()*3 + 1);
		System.out.println(x);
		int x1 = 12 ;
		int x2 = 3 ;
		System.out.println(Math.max(x1,  x2));
		String n1 = "bonjour" ;
		String n2 = "au revoir" ;
		int res = n1.compareTo(n2) ;
		if (res > 0) {
			System.out.println("n1 est apres n2");
		}
		else {
			if(res < 0) {
				System.out.println("n1 est avant n2");
			}
			else {
				System.out.println("n1 est egale a n2");
			}
		}
	}
}
