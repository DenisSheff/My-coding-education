package org.example.seminar1.cw1;

//https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        System.out.print("Input a number here: ");
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int sum = 0;
        int product = 1;
        while (number != 0) {
            product *= number % 10;
            sum += number % 10;
            number /= 10;
        }
        System.out.print("Output is: " + (product - sum));
    }
}
