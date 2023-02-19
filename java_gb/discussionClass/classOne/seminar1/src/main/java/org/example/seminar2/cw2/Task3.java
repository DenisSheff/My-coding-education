package org.example.seminar2.cw2;

//3) Дан массив целых чисел.
// Найти количество пар соседних элементов, где первый элемент вдвое больше второго.

import java.util.Scanner;

public class Task3 {
    public static void main(String[] args) {
        int counter = 0;
        Scanner scanner = new Scanner(System.in);
        int amount = scanner.nextInt();
        int[] myArray = new int[amount];
        for (int i = 0; i < amount; i++) {
            myArray[i] = scanner.nextInt(); 
        }
        for (int i = 0; i < amount - 1; i++) {
            if (myArray[i] == 2 * myArray[i + 1]) {
                counter++;
            }
        }
        scanner.close();
        System.out.println(counter);
    }
}
