package org.example.seminar3.hw3.task1;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Item item1 = new Item("High quality chicken", 150.90, 3);
        Item item2 = new Item("Pork", 190.70, 3);
        Item item3 = new Item("Chicken", 100.0, 3);
        Item item4 = new Item("High quality pork", 470.50, 1);
        Item item5 = new Item("High quality beef", 400.0, 2);
        Item item6 = new Item("Beef", 210.50, 1);
        Item item7 = new Item("Pork", 350.20, 1);
        Item item8 = new Item("Beef", 270.90, 3);

        List<Item> groceriesList = new ArrayList<>();
        groceriesList.add(item1);
        groceriesList.add(item2);
        groceriesList.add(item3);
        groceriesList.add(item4);
        groceriesList.add(item5);
        groceriesList.add(item6);
        groceriesList.add(item7);
        groceriesList.add(item8);

        Double highestPrice = 0.0;

        for (int i = 0; i < groceriesList.size(); i++) {
            String keyWord = groceriesList.get(i).getName();
            Integer keyCategory = groceriesList.get(i).getCategory();
            if (keyWord.equals("High")
                && keyCategory.equals(1)
                || keyCategory.equals(2)) {
                    if (groceriesList.get(i).getPrice() > highestPrice) {
                        highestPrice = groceriesList.get(i).getPrice();
                    }
            }
        }
        System.out.println(groceriesList);
        System.out.println(highestPrice);
    }
}
