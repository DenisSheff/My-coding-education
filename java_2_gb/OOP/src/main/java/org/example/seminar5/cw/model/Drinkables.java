package org.example.seminar5.cw.model;

import java.math.BigDecimal;

public class Drinkables extends Product {
    private Double volume;
    public Drinkables(String name, BigDecimal price, Double volume) {
        super(name, price);
        this.volume = volume;
    }
    public Double getVolume() {
        return volume;
    }
    @Override
    public String toString() {
        return super.toString() + "объем = " + volume + " ";
    }
    public void setVolume(Double volume) {
        if (volume > 0) this.volume = volume;
        else System.out.println("Объем напитка не может быть равен или меньше нуля!");
    }
}
