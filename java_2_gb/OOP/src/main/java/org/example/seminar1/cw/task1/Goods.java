package org.example.seminar1.cw.task1;


import lombok.AllArgsConstructor;
import lombok.Data;

@AllArgsConstructor
@Data
public class Goods {
    private String name;
    private int price;
    @Override
    public String toString() {
        return "Product {" +
                "name: " + name + '\'' +
                ", price: " + price + '\'' +
                "}";
    }
}
