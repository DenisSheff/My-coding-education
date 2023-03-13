package org.example.seminar1.cw.task2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        PublicVendingMachine publicVendingMachine = new PublicVendingMachine();
        List<BottleOfWater> bottleOfWaters = new ArrayList<>(Arrays.asList(new BottleOfWater("Aqua", 100),
                new BottleOfWater("Spring Water", 150),
                new BottleOfWater("Aqua Minerale", 100)));
        publicVendingMachine.initProduct(bottleOfWaters);
        System.out.println(publicVendingMachine.getGoods("Spring Water").toString());
    }
}
