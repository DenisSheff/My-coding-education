package org.example.seminar1.cw.task1;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.ArrayList;
import java.util.List;

@AllArgsConstructor
@Data
public class VendingMachine {
    List<Goods> goods = new ArrayList<>();

    public VendingMachine() {

    }

    public void intProduct(List<Goods> goods) {
        this.goods = goods;
    }
    public Goods getGoods(String name) {
        for (Goods p : goods) {
            if (p.getName().equals(name)) {
                return p;
            }
        }
        return new Goods("There is no a such item", 0);
    }
}
