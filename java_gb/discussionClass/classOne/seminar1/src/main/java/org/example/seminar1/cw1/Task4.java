package org.example.seminar1.cw1;

import java.util.Scanner;

//Given two binary strings a and b, return their sum as a binary string.
public class Task4 {
    public static void main(String[] args) {
        System.out.println(addBinary("11", "1"));
    }
    public static String addBinary(String a, String b) {
        if (a.length() < b.length()) {
            return addBinary(b, a);
        }
        String result = "";
        int counter = 0;
        int j = b.length() - 1;
        for (int i = a.length() - 1; i >= 0; i--) {
            if (a.charAt(i) == '1') {
                counter++;
            }
            if (j >= 0 && b.charAt(j) == '1') {
                counter++;
            }
            result = counter % 2 + result;
            j--;
            counter /= 2;
        }
        if (counter > 0) {
            result = counter + result;
        }
        return result;
    }
}
