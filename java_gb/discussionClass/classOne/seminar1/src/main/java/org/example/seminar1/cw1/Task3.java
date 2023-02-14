package org.example.seminar1.cw1;

import java.util.Scanner;

//Дана строка. Поменять местами ее половины.
public class Task3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String myString = scanner.nextLine();
        StringBuilder newString = new StringBuilder();
        newString
                .append(myString.substring(myString.length() / 2, myString.length()))
               .append(myString.substring(0, myString.length() / 2));
        System.out.println(newString.toString());
    }
}
