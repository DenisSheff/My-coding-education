package org.example;

public class Main {
    public static void main(String[] args) {
        System.out.println(subtractProductAndSum(234));

    }
    public static int subtractProductAndSum(int n) {
        int sum = 0;
        int product = 1;
        int result = product - sum;
        while (n != 0) {
            product *= (n % 10);
            sum += (n % 10);
            n /= 10;
        }

        System.out.println(sum);
        System.out.println(product);
        return product - sum;
    }
}