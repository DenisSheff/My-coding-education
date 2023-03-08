package org.example.seminar6.cw.task4;

public class Réaumur implements Converter{
    @Override
    public double convertValue(double val) {
        return val / 0.80000;
    }
}
