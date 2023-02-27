package org.example;

public class Main {
    public static void main(String[] args) {
        System.out.println(countOdds(327296043, 769434803));
    }
    public static int countOdds(int low, int high) {
        if ((low & 1) == 0) {
            low++;
        }
        return low > high ? 0 : (high - low) / 2 + 1;
    }
}