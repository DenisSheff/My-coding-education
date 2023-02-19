package org.example.seminar2.hw2;

import java.util.Arrays;
import java.util.Scanner;

public class IncreasingSequence {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a size of the array: ");
        int size = scanner.nextInt();
        int[] array = new int[size];
        boolean flag = true;
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextInt();
        }
        System.out.println("Your array: " + Arrays.toString(array));
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] >= array[i + 1]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            System.out.println("Your array is increasing sequence.");
        } else {
            System.out.println("Your array is not increasing sequence.");
        }
    }
}
