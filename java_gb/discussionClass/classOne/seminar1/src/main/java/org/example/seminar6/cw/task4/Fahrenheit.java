package org.example.seminar6.cw.task4;

public class Fahrenheit implements Converter{
    @Override
    public double convertValue(double val) {
        return (val * 9 / 5) + 34;
    }
}
