package exercice1;

public class Robot {
	
	public String reference;
    public String name;
    public int x, y;
    public int orientation;
    private static int nb_robots = 0;

    public static final int NORD = 1;
    public static final int EST = 2;
    public static final int SUD = 3;
    public static final int OUEST = 4;

    public Robot(String name, int x, int y, int orientation){

        this.name = name;
        this.x = x;
        this.y = y;
        this.orientation = orientation;

        nb_robots+=1;

        this.reference = "ROB"+nb_robots;
    }

    public Robot(String name){

        this.x = 0;
        this.y = 0;
        this.orientation = 1;
        this.name = name;

        nb_robots+=1;

        this.reference ="ROB"+nb_robots;

    }

    public void modifOrientation(int orientation){
        this.orientation = orientation;
    }

    public void modifPosition(){
        if(this.orientation == NORD){
            this.y +=1;
        }
        if(this.orientation == EST){
            this.x +=1;
        }
        if(this.orientation == SUD){
            if(this.y - 1 < 0){
                System.out.println("Déplacement impossible vous ne pouvez pas être en dessous de 0");
            }
            else{
                this.y-=1;
            }
        }
        if(this.orientation==OUEST){
            if(this.x - 1 < 0){
                System.out.println("Déplacement impossible vous ne pouvez pas être en dessous de 0");
            }
            else{
                this.x-=1;
            }
        }
    }

    public String afficheToi(){
        return String.format("Nom du robot : %s | Référence : %s | Coordonnées x, y : %d %d | Orientation : %d", this.name, this.reference, this.x, this.y, this.orientation);
    }
}
