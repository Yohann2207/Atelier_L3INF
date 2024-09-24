import java.util.ArrayList;
import java.util.Random;

/**
 * Représente un jeu où plusieurs joueurs déplacent leurs personnages sur un plateau composé de cases.
 * Chaque case peut contenir un obstacle ou un gain, et les joueurs accumulent des points tout au long des étapes du jeu.
 */
public class Jeu {

    /**
     * Le titre du jeu.
     */
    private String titre;

    /**
     * Le nombre maximal de joueurs pouvant participer au jeu.
     */
    private static final int NB_JOUEUR_MAX = 6;

    /**
     * Le nombre total de cases sur le plateau de jeu.
     */
    private static final int NB_CASES = 50;

    /**
     * La liste des joueurs participant au jeu.
     */
    private ArrayList<Joueur> listeJoueurs;

    /**
     * Le tableau représentant les cases du plateau.
     */
    private Case[] cases;

    /**
     * Le nombre total d'étapes du jeu.
     */
    private int nbEtapes;

    /**
     * Le nombre total d'obstacles à ajouter sur le plateau.
     */
    private int nbObstacles;

    /**
     * Le score maximum atteint par un joueur dans le jeu.
     */
    private int scoreMax;

    /**
     * Constructeur pour créer un nouveau jeu avec un titre, un nombre d'étapes et d'obstacles.
     * 
     * @param titre le titre du jeu
     * @param nbEtapes le nombre d'étapes du jeu
     * @param nbObstacles le nombre d'obstacles à placer sur le plateau
     */
    public Jeu(String titre, int nbEtapes, int nbObstacles) {
        this.titre = titre;
        this.nbEtapes = nbEtapes;
        this.nbObstacles = nbObstacles;
        this.listeJoueurs = new ArrayList<>();
        this.cases = new Case[NB_CASES];
    }

    /**
     * Ajoute un joueur à la liste des joueurs du jeu.
     * 
     * @param j le joueur à ajouter
     */
    public void ajouterJoueur(Joueur j) {
        listeJoueurs.add(j);
    }

    /**
     * Retourne une liste contenant tous les personnages des joueurs.
     * 
     * @return une liste de tous les personnages du jeu
     */
    public ArrayList<Personnage> tousLesPerso() {
        ArrayList<Personnage> res = new ArrayList<>();
        for (Joueur joueur : listeJoueurs) {
            res.addAll(joueur.getListePerso());
        }
        return res;
    }

    /**
     * Initialise les cases du plateau avec des gains aléatoires et place les obstacles.
     */
    public void initialiserCases() {
        Random rand = new Random();
        int obstaclesAjoutes = 0;
        for (int i = 0; i < NB_CASES; i++) {
            int montantGains = rand.nextInt(NB_CASES) + 1;
            cases[i] = new Case(montantGains);
            if (montantGains % 5 == 0 && obstaclesAjoutes < nbObstacles) {
                int penalite = montantGains * 2;
                Obstacle obstacle = new Obstacle(penalite);
                cases[i].setObstacle(obstacle);
                obstaclesAjoutes++;
            }
        }
        System.out.println("Cases initialisees avec " + obstaclesAjoutes + " obstacles.\n");
    }

    /**
     * Lance le jeu, en plaçant d'abord les personnages sur les cases libres, puis en déroulant les étapes.
     */
    public void lancerJeu() {
        initialiserCases();
        for (Joueur joueur : listeJoueurs) {
            ArrayList<Personnage> listePersos = joueur.getListePerso();
            for (Personnage personnage : listePersos) {
                for (int i = 0; i < NB_CASES; i++) {
                    if (cases[i].estLibre()) {
                        cases[i].placerPersonnage(personnage);
                        personnage.setPosition(i);
                        break;
                    }
                }
            }
        }

        // Dérouler les étapes du jeu
        ArrayList<Personnage> listePersos = tousLesPerso();
        for (int etape = 0; etape < nbEtapes; etape++) {
            for (Personnage personnage : listePersos) {
                int positionSouhaitee = personnage.positionSouhaitee();

                // Vérifier si la position souhaitée dépasse la dernière case
                if (positionSouhaitee >= cases.length) {
                    positionSouhaitee = cases.length - 1;
                }

                Case caseSouhaitee = cases[positionSouhaitee];

                if (caseSouhaitee.estLibre()) {
                    // Si la case est libre, déplacer le personnage et ajouter les gains
                    personnage.deplacer(positionSouhaitee, caseSouhaitee.getGain());
                } else if (!caseSouhaitee.sansObstacle()) {
                    // Si la case a un obstacle, appliquer la pénalité
                    personnage.penaliser(caseSouhaitee.getPenalite());
                } else {
                    // Si la case est occupée par un autre personnage, appliquer une pénalité équivalente au gain
                    personnage.penaliser(caseSouhaitee.getGain());
                }
            }
        }

        afficherResultats();
    }

    /**
     * Affiche l'état de toutes les cases du plateau de jeu.
     */
    public void afficherCases() {
        for (Case aCase : cases) {
            System.out.println(aCase.toString());
        }
    }

    /**
     * Affiche la liste des participants (joueurs) dans le jeu.
     */
    public void afficherParticipants() {
        System.out.println("LISTE DES JOUEURS -------------------------");
        for (Joueur joueur : listeJoueurs) {
            System.out.println(joueur.toString());
        }
        System.out.println("------------------------------------------");
    }

    /**
     * Affiche les résultats du jeu, y compris le joueur gagnant et si un record a été battu.
     */
    public void afficherResultats() {
        afficherCases();
        System.out.println("\n");
        afficherParticipants();
        
        Joueur gagnant = null;
        for (Joueur joueur : listeJoueurs) {
            if (gagnant == null || joueur.getPoints() > gagnant.getPoints()) {
                gagnant = joueur;
            }
        }
        
        if (gagnant != null && gagnant.getPoints() > scoreMax) {
            scoreMax = gagnant.getPoints(); 
        }

        System.out.println("\nJEU " + titre);
        System.out.println("***********************************************");
        System.out.println("RESULTATS");
        if (gagnant != null) {
            System.out.println("Le gagnant est " + gagnant.getNom() + " avec " + gagnant.getPoints() + " points");
            if (gagnant.getPoints() > scoreMax) {
                System.out.println("Record battu : Ancien score maximum " + scoreMax);
            }
        }
    }
}
