package org.example.seminar5.cw.model;
import java.math.BigDecimal;

public abstract class Product {
    private String name;
    private BigDecimal price;
    public Product() {
    }
    public Product(String name, BigDecimal price) {
        this.name = name;
        this.price = price;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public BigDecimal getPrice() {
        return price;
    }
    public void setPrice(BigDecimal price) {
        if (price.compareTo(BigDecimal.valueOf(0)) > 0) this.price = price;
        else System.out.println("Стоимость не может быть равна или меньше нуля!");
    }
    @Override
    public String toString() {
        return "\"" + name + "\" стоит: " + price + " у.е. ";
    }
}
