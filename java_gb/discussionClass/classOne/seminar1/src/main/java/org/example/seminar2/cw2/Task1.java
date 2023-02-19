package org.example.seminar2.cw2;

//mplement pow(x, n), which calculates x raised to the power n (i.e., xn).

import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input a number: ");
        double number = scanner.nextDouble();
        System.out.print("Input a power the number is needed to be raised: ");
        int degree = scanner.nextInt();
        double result = 1;
        scanner.close();
        if (degree < 0) {
            number = 1 / number;
            degree *= -1;
        }
        for (int i = 0; i < degree; i++) {
            result *= number;
        }
        System.out.println("Result is: " + result);
    }
}
