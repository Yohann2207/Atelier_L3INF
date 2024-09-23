package exercice2;

public class Vecteur3D {
	
	private int x ;
	
	private int y ;
	
	private int z ;
	
	
	
	public Vecteur3D(int x, int y, int z) {
		this.x = x ;
		this.y = y ;
		this.z = z ;
	}
	
	public Vecteur3D() {
		this(0, 0, 0);
	}
	
	public void affiche() {
		 System.out.println("<" + x + "," + y + "," + z + ">" );
	}
	
	public double norme() {
		return Math.sqrt(Math.pow(x, 2) + Math.pow(y,  2) + Math.pow(z, 2)) ;
	}
	
	public static double produitScalaire(Vecteur3D v1, Vecteur3D v2) {
		return (v1.x * v2.x + v1.y * v2.y + v1.z * v2.z) ; 
	}
	
	public double produitScalaire(Vecteur3D v2) {
		return (this.x * v2.x + this.y * v2.y + this.z * v2.z) ;
	}
	
	public static Vecteur3D somme(Vecteur3D v1, Vecteur3D v2) {
		Vecteur3D n = new Vecteur3D() ;
		n.x = v1.x + v2.x ;
		n.y = v1.y + v2.y ;
		n.z = v1.z + v2.z ;
		return n ;
	}
	
	public Vecteur3D somme(Vecteur3D v2) {
		Vecteur3D n = new Vecteur3D() ;
		n.x = this.x + v2.x ;
		n.y = this.y + v2.y ;
		n.z = this.z + v2.z ;
		return n ;
	}
	
	public String toString() {
		return "<" + this.x + "," + this.y + "," + this.z + ">" ;
	}
}
