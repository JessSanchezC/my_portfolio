import java.util.*;

public class OddAndEvens {
    public static void main(String[] args){
        //intro
        Scanner input = new Scanner(System.in);
        System.out.println("Let’s play a game called “Odds and Evens”");
        System.out.print("What is your name? ");
        String name=input.nextLine();

        //PICK:
        System.out.print("Hi "+name+", which do you choose? (O)dds or (E)vens? ");
        String player1=input.next();

        int x=1;
        while(x==1) {
            if (player1.equalsIgnoreCase("O")){
                System.out.println(name+" has picked odds! The computer will be evens.");
                x=0;
            } else if (player1.equalsIgnoreCase("E")) {
                System.out.println(name + " has picked Evens! The computer will be Odds.");
                x=0;
            } else {
                System.out.println("**** E R R O R ! ****");
                System.out.print("Try again " + name + ", which do you choose? (O)dds or (E)vens? ");
                player1 = input.next();
            }

        }

        System.out.println("----------------------------------\n");

        //User plays, choose finger <=5
        int user;
        System.out.print("How many “fingers” do you put out? ");
        user= input.nextInt();

        int y=1;
        while (y==1){
            if(user<=5){
                y=0;
            } else {
                System.out.println("**** E R R O R ! ****");
                System.out.println("Maximum 5 fingers in one hand!!! Try again " + name+ "!");
                System.out.print("How many “fingers” do you put out? ");
                user= input.nextInt();
            }
        }

        //computer choose a random number to represent their fingers:
        Random rand = new Random();
        int computer = rand.nextInt(6);
        System.out.print("The computer plays number "+computer);
        System.out.println("\n----------------------------------\n");

        //sum user fingers + computer fingers and define if result is even or odd nd winner
        int sum=user+computer;
        System.out.println(user+"+"+computer+"="+sum);
        String result;
        String winner="";

        if (sum%2==0){
            result="even";
            if (player1.equalsIgnoreCase("e")){
                winner=name;
            } else if (player1.equalsIgnoreCase("o")){
                winner="computer";
            }
        } else {
            result = "odd";
            if (player1.equalsIgnoreCase("o")){
                winner=name;
            } else if (player1.equalsIgnoreCase("e")) {
                winner = "computer";
            }
        }

        System.out.println(sum+" is ..."+result+"!");
        System.out.println("That means "+winner+ " wins!:)");


        System.out.println("----------------------------------\n");


    }

}
