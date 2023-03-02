package org.example;

public class Main {
    public static void main(String[] args) {
        int[] arr = new int[] {5000, 2000, 1000, 10000};
        System.out.println(average(arr));

    }
    public static double average(int[] salary) {
        int max = salary[salary.length - 1];
        int min = salary[0];
        double totalSum = 0;
        for (int i = 1; i < salary.length; i++) {
            totalSum += salary[i];
            if (salary[i] > max) {
                max = salary[i];
            }
            if (salary[i] < min) {
                min = salary[i];
            }
        }
        totalSum = totalSum - max - min;
        return totalSum / (salary.length - 2);
    }
}