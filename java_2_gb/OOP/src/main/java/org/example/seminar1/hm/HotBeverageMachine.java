package org.example.seminar1.hm;

import java.util.ArrayList;
import java.util.List;

public class HotBeverageMachine extends VendingMachine {
    List<HotBeverage> hotBeverages = new ArrayList<>();
    @Override
    void initProduct(List<HotBeverage> hotBeverages) {
        this.hotBeverages = hotBeverages;
    }


    @Override
    String getGoods(String name) {
        for (HotBeverage p : hotBeverages) {
            if (p.getName().equals(name)) {
                return p.getName() + " " + p.getPrice() + " " + p.getTemperature();
            }
        }
        return new HotBeverage("Not found!", 0, 0).toString();
    }
}
