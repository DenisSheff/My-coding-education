package org.example.seminar2.hw2;


import java.util.Scanner;

public class SimpleNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a last number of a range: ");
        int rangeEnd = scanner.nextInt();
        int sum = 0;
        for (int checkNumber = 2; checkNumber <= rangeEnd; checkNumber++) {
            boolean isPrime = true;
            for (int i = 2; i < checkNumber; i++) {
                if (checkNumber == 0 || checkNumber == 1) {
                    isPrime = false;
                } else if (checkNumber % i == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                sum += checkNumber;
            }
        }
        System.out.println("\nThe sum of Prime Numbers is " + sum);
    }
}
