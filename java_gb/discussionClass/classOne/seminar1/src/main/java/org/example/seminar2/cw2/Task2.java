package org.example.seminar2.cw2;

//2) Дана последовательность из N целых чисел.
// Найти сумму чисел, оканчивающихся на 5, перед которыми идет четное число.

import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input amount of numbers: ");
        int numberAmount = scanner.nextInt();
        System.out.print("Input list of numbers: ");
        int number = scanner.nextInt();
        int sum = 0;
        for (int i = 1; i < numberAmount; i++) {
            int numberTwo = scanner.nextInt();
            if (number % 2 == 0 && numberTwo % 10 == 5) {
                sum += numberTwo;
            }
            number = numberTwo;
        }
        scanner.close();
        System.out.println(sum);
    }
}
