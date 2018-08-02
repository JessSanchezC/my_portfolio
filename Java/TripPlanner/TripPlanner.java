//Created on 25.01.2017, Assignment1//

import java.util.Scanner;

public class TripPlanner {
    public static void main(String[]args){
        greeting();
        timeBudget();
        timeDifference();
        countryArea();


    }

    public static void greeting(){
        //Takes in user name and destination//
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Vacation Planner!");
        System.out.print("What is your name? ");
        String name = input.nextLine();
        System.out.print("Nice to meet you "+name+", where are you travelling to? ");
        String destination = input.nextLine();
        System.out.println("Great! "+destination+" sounds like a great trip");
        System.out.println("***********\n");

    }

    public static void timeBudget(){
        Scanner input = new Scanner(System.in);
        //takes in days planned on trip, allowance and converting info//
        System.out.print("How many days are you going to spend travelling? ");
        int days = input.nextInt();
        System.out.print("How much money, in USD, are you planning to spend on your trip? ");
        double USD = input.nextDouble();
        System.out.print("What is the three letter currency symbol for your travel destination? ");
        String currency = input.next();
        System.out.print("How many "+currency+" are there in 1 USD? ");
        double xrate = input.nextDouble();
        System.out.println();

        int hours=days*24;
        int minutes=hours*60;
        System.out.println("If you are travelling for "+days+" days that is the same as "+hours+" hours or "+minutes+" minutes");
        System.out.println("if you are going to spend $"+USD+" USD that means per day you can spend up to "+((int)(USD/days*100)/100.0)+" USD");
        System.out.println("Your total budget in "+currency+" is "+((int)(USD*xrate*100)/100.0)+" "+currency+", which per day is "+((int)((USD*xrate)/days*100)/100.0)+" "+currency);

        System.out.println("***********\n");
    }

    public static void timeDifference(){
        Scanner input = new Scanner(System.in);
        //takes in the time difference between home and destination//
        System.out.print("What is the time difference, in hours, between your home and your destination? ");
        int difference=input.nextInt();

        int x=(24+difference)%24;
        int y=(24+12+difference)%24;
        System.out.println("That means that when it is midnight at home it will be "+x+":00 in your travel destination and when it is noon at home  it will be "+y+":00");


        System.out.println("***********\n");
    }

    public static void countryArea(){
        Scanner input = new Scanner(System.in);
        //takes in the distance between user home and destination in square km and convert it into square miles//
        //km*0,62137=miles//

        System.out.print("What is the square area of your destination country in km2? ");
        double area=input.nextDouble();
        System.out.println("In miles2 that is "+((int)((area*0.62137*0.62137)*10)/10.0));

        System.out.println("***********\n\n");

    }


}
