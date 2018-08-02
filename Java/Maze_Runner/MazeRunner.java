import java.util.*;

public class MazeRunner {
    static Maze myMap = new Maze();
    static Scanner input= new Scanner(System.in);


    public static void main (String[] args){

        intro(); //intro and print map

        //Repeat the process of asking a user where they would like to move until you reach the end of the game.
        // You will know you’ve won when the method myMap.didIWin() returns true.
        // Until you win that method will return false.
        int moves=0;
        int x=0;

        while (x==0) {
            if (!myMap.didIWin() && moves < 100) {
                userMover(); //ask for movement, make sure you can move that way according to the map.
                moves++;
                myMap.printMap();//print updated map
                movesMessage(moves);
            } else if (myMap.didIWin()) {
                System.out.println("Congratulations, you made it out alive!");
                System.out.println("You win using "+moves+" moves!");
                x++;
            } else if (moves == 100) {
                System.out.println("Sorry, but you didn't escape in time- you lose!");
                x++;
            }
        }

    }


    public static void intro(){
        //welcome the user and print new map

        System.out.println("Welcome to Maze Runner!");
        System.out.println("Here is your current position:");
        myMap.printMap();
    }

    public static String userMover() {
        //take desired direction to move:
        System.out.print("Where would you like to move? (R, L, U, D)");
        String direction = input.nextLine();

        //Guarantee that the user selection is only one of the given options,
        //and continue to reprompt the user until they enter a desired direction.
        //if you cannot move in that direction, notify the user there is wall in that direction and ask them to pick a new direction to move.

        if (direction.equals("R")||direction.equals("L")||direction.equals("U")||direction.equals("D")){
            if (direction.equals("R")&&(myMap.canIMoveRight())){
                myMap.moveRight(); // Moves your position one to the right and prints out the new board
            } else if (direction.equals("L")&&(myMap.canIMoveLeft())) {
                myMap.moveLeft(); // Moves your position one to the left and prints out the new board
            }else if (direction.equals("U")&&(myMap.canIMoveUp())){
                myMap.moveUp(); // Moves your position one above and prints out the new board
            } else if (direction.equals("D")&&(myMap.canIMoveDown())){
                myMap.moveDown(); // Moves your position one below and prints out the new board
            } else if(myMap.isThereAPit(direction)){
                navigatePit(direction);
            } else {
                System.out.println("Sorry, you’ve hit a wall.");
                myMap.printMap();
                userMover();
            }
        } else {
            System.out.println("\nWrong input! ");
            userMover();
        }

        //return a string indicating which direction the user chooses to move in
        return direction;

    }

    public static int movesMessage(int moves){
        //print message after certain number of moves
        //count moves

        int nMoves=moves;

        if (nMoves==50){
            System.out.println("\nWarning: You have made 50 moves, you have 50 remaining before the maze exit closes");
        } else if (nMoves==75){
            System.out.println("\nAlert! You have made 75 moves, you only have 25 moves left to escape.");
        } else if (nMoves==90) {
            System.out.println("\nDANGER! You have made 90 moves, you only have 10 moves left to escape!!");
        } else if (nMoves==90) {
            System.out.println("\nOh no! You took too long to escape, and now the maze exit is closed FOREVER >:[");
        }else if (nMoves==100) {
            System.out.println("\nOh no! You took too long to escape, and now the maze exit is closed FOREVER >:[");
        }


        return nMoves;
    }

    public static void navigatePit(String direction){

        System.out.print("Watch out! There's a pit ahead, jump it? (Y/N)");
        String jump= input.nextLine();

        if (jump.startsWith("Y")){
            myMap.jumpOverPit(direction);
        } else if (jump.startsWith("N")) {
            userMover();
        } else {
            System.out.println("Please type \"Y\" or \"N");
            navigatePit(direction);
        }

    }

}
