package org.example.seminar1.hw1;

//Дана последовательность целых чисел, оканчивающаяся нулем. Найти сумму положительных чисел, после которых следует отрицательное число.
//Пример: 1 2 1 2 -1 1 3 1 3 -1 0
//2 -1 переход - 2 в сумму
//3 -1 переход 3 в сумму
//суммарно выведет 5

import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numbersAmount = scanner.nextInt();
        int firstNumber = scanner.nextInt();
        int counter = 0;
        for (int i = 1; i < numbersAmount; i++) {
            int secondNumber = scanner.nextInt();
            if (firstNumber > 0 && secondNumber < 0) {
                counter += firstNumber;
            }
            firstNumber = secondNumber;
        }
        System.out.println(counter);
    }
}
