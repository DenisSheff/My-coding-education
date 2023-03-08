package org.example.seminar6.cw.task4;

public class Main {
    public static void main(String[] args) {
        double temperature = 37;
        System.out.println(new Fahrenheit().convertValue(temperature));
        System.out.println(new Celsius().convertValue(temperature));
        System.out.println(new Kelvin().convertValue(temperature));
        System.out.println(new Réaumur().convertValue(temperature));
    }
}
