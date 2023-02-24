package org.example.seminar3.cw3.task1;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Items items = new Items("qwe", "asd", 3);
        Items items1 = new Items("qwe1", "asd1", 3);
        Items items2 = new Items("qwe", "asd", 3);
        Items items4 = new Items("qwe", "fsdfsd", 10);
        List<Items> itemsList = new ArrayList<>();
        itemsList.add(items);
        itemsList.add(items1);
        itemsList.add(items2);
        itemsList.add(items4);
        System.out.println(itemsList);
        String searchItem = "qwe";
        Integer sumValue = 0;
        List<String> country = new ArrayList<>();
        for (int i = 0; i < itemsList.size(); i++) {
            if (itemsList.get(i).getName().equals(searchItem)) {
                sumValue += itemsList.get(i).getValue();
                boolean flag = true;
                for (int j = 0; j < country.size(); j++) {
                    if (itemsList.get(i).getCountry().equals(country.get(j))) {
                        flag = false;
                    }
                }
                if (flag) {
                    country.add(itemsList.get(i).getCountry());
                }
            }
        }
        System.out.println(country);
        System.out.println(sumValue);
    }
}
