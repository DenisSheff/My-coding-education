package org.example.seminar6.cw.task4;

public class Kelvin implements Converter{
    @Override
    public double convertValue(double val) {
        return (val + 273.15);
    }
}
