package org.example.seminar1.hm;

public class HotBeverage {
    private String name;
    private int price;
    private int temperature;
    public HotBeverage(String name, int price, int temperature) {
        this.name = name;
        this.price = price;
        this.temperature = temperature;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public int getTemperature() {
        return temperature;
    }

    public void setTemperature(int temperature) {
        this.temperature = temperature;
    }
}
