package exercice2;

import java.text.DecimalFormat;

public class testVecteur3D {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Vecteur3D v1 = new Vecteur3D(3, 2, 5);
		Vecteur3D v2 = new Vecteur3D(1, 2, 3);
		DecimalFormat df = new DecimalFormat("#0.00"); 
		System.out.println("v1 = " + v1);
		System.out.println("Norme de v1 = " + df.format(v1.norme()));
		System.out.println("v2 = " + v2);
		System.out.println("Norme de v2 = " + df.format(v2.norme()));
		System.out.println("v1 + v2 = " + Vecteur3D.somme(v1,  v2));
		System.out.println("v1 + v2 = " + v1.somme(v2));
		System.out.println("v1.v2 = " + v1.produitScalaire(v2));
		System.out.println("v1.v2 = " + Vecteur3D.produitScalaire(v1, v2));
	}

}
