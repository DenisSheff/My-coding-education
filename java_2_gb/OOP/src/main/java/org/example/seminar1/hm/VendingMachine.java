package org.example.seminar1.hm;


import java.util.ArrayList;
import java.util.List;

public abstract class VendingMachine {
    private List<HotBeverage> bottle = new ArrayList<>();
    abstract void initProduct(List<HotBeverage> bottle);
    abstract String getGoods(String name);
}
