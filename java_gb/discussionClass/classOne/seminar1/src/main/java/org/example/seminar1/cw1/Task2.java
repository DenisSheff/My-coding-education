package org.example.seminar1.cw1;

import java.util.Scanner;

//Дана последовательность N целых чисел.
// Найти количество положительных чисел,
// после которых следует отрицательное число.

public class Task2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int numberOne = scanner.nextInt();
        int counter = 0;
        for (int i = 1; i < number; i++) {
            int numberTwo = scanner.nextInt();
            if (numberOne > 0 && numberTwo < 0) {
                counter++;
            }
            numberOne = numberTwo;
        }
        System.out.println(counter);
    }
}
