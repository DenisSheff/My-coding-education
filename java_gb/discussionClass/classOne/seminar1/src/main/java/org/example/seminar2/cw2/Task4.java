package org.example.seminar2.cw2;

public class Task4 {
    public static void main(String[] args) {
        Vector vector1 = new Vector(1, 3, 9);
        Vector vector2 = new Vector(3, 3, 3);
        System.out.println(vector1.toString());
        System.out.println(vector1.length());
        System.out.println(vector1.scalarProduct(vector2));
        System.out.println(vector1.vectorProduct(vector2));
        System.out.println(vector1.cos(vector2));
        System.out.println(vector1.vectorSum(vector2));
        System.out.println(vector1.vectorDifference(vector2));
    }


}
