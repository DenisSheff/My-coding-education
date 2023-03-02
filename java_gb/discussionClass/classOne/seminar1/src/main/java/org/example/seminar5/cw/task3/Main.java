package org.example.seminar5.cw.task3;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input a number here: ");
        String text = sc.nextLine();
        System.out.println("Result is " + change(text));
    }

    public static int change(String str) {
        Map<Character, Integer> mapList = new HashMap<>();
        mapList.put('I', 1);
        mapList.put('V', 5);
        mapList.put('X', 10);
        mapList.put('L', 50);
        mapList.put('C', 100);
        mapList.put('D', 500);
        mapList.put('M', 1000);
        int num = mapList.get(str.charAt(str.length() - 1));
        for (int i = 0; i < str.length() - 1; i++) {
            if (mapList.get(str.charAt(i + 1)) > mapList.get(str.charAt(i))) {
                num -= mapList.get(str.charAt(i));
            } else {
                num += mapList.get(str.charAt(i));
            }
        }
        return num;
    }
}
