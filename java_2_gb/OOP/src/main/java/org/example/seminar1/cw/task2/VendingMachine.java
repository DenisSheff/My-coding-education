package org.example.seminar1.cw.task2;

import java.util.ArrayList;
import java.util.List;

public abstract class VendingMachine {
    private List<BottleOfWater> bottle = new ArrayList<>();
    abstract void initProduct(List<BottleOfWater> bottle);
    abstract String getGoods(String name);
}
