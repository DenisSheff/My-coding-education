package org.example.seminar1.hm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        HotBeverageMachine hotBeverageMachine = new HotBeverageMachine();
        List<HotBeverage> hotBeverages = new ArrayList<>(Arrays.asList(
                new HotBeverage("doppio", 150, 90),
                new HotBeverage("latte", 250, 80),
                new HotBeverage("espresso", 90, 100)));
        hotBeverageMachine.initProduct(hotBeverages);
        System.out.println(hotBeverageMachine.getGoods("doppio"));
    }
}
