package org.example.seminar1.cw.task1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Goods> goods = new ArrayList<>(Arrays.asList(new Goods("Pepsi", 42),
                new Goods("Lays", 90),
                new Goods("Coke", 65),
                new Goods("Nuts", 67)));
        VendingMachine vendingMachine = new VendingMachine();
        vendingMachine.intProduct(goods);
        System.out.println(vendingMachine.getGoods("Lays"));
    }
}
