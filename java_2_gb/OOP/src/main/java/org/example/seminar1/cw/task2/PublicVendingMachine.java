package org.example.seminar1.cw.task2;

import java.util.ArrayList;
import java.util.List;

public class PublicVendingMachine extends VendingMachine {
    List<BottleOfWater> bottle = new ArrayList<>();
    @Override
    void initProduct(List<BottleOfWater> bottle) {
        this.bottle = bottle;
    }

    @Override
    String getGoods(String name) {
        for (BottleOfWater p : bottle) {
            if (p.getName().equals(name)) {
                return p.getName() + " " + p.getPrice();
            }
        }
        return new BottleOfWater("Not found!", 0).toString();
    }
}
