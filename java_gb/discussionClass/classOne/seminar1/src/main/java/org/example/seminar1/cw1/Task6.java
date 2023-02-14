package org.example.seminar1.cw1;

import java.util.Scanner;

//Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
//Return the running sum of nums.
public class Task6 {
    public static void main(String[] args) {
        System.out.println(runningSum());
    }
    public static int[] runningSum() {
        Scanner scanner = new Scanner(System.in);
        int arraySize = scanner.nextInt();
        int[] myArray = new int[arraySize];
        int[] resultArray = new int[myArray.length];
        int sum = 0;
        for (int i = 0; i < myArray.length; i++) {
            myArray[i] = scanner.nextInt();
            sum += myArray[i];
            resultArray[i] = sum;
        }
//        resultArray[0] = myArray[0];
//        for (int i = 1; i < myArray.length; i++) {
//            resultArray[i] = myArray[i] + resultArray[i - 1];
//        }
        for (int i = 0; i < resultArray.length; i++) {
            System.out.println(resultArray[i]);
        }
        return null;
    }
}
