import java.util.Scanner;

public class teste {
    int idade = 45;

    public static void printName() {
        Scanner input = new Scanner(System.in);

        System.out.print("Insert your first name here: ");
        String firstName = input.next();

        System.out.print("Insert your last name here: ");
        String lastName = input.next();

        System.out.println("Your full name is " + firstName + " " + lastName);

        input.close();
    }

}

