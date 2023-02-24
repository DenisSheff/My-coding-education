package org.example.seminar3.hw3.task2;

import org.example.seminar3.hw3.task1.Item;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Item item1 = new org.example.seminar3.hw3.task1.Item("High quality chicken", 150.90, 2);
        Item item2 = new org.example.seminar3.hw3.task1.Item("Pork", 190.70, 3);
        Item item3 = new org.example.seminar3.hw3.task1.Item("Chicken", 100.0, 3);
        Item item4 = new org.example.seminar3.hw3.task1.Item("High quality pork", 470.50, 1);
        Item item5 = new org.example.seminar3.hw3.task1.Item("High quality beef", 400.0, 2);
        Item item6 = new org.example.seminar3.hw3.task1.Item("Beef", 210.50, 1);
        Item item7 = new org.example.seminar3.hw3.task1.Item("Pork", 350.20, 1);
        Item item8 = new org.example.seminar3.hw3.task1.Item("Beef", 270.90, 3);

        List<Item> groceriesList = new ArrayList<>();
        groceriesList.add(item1);
        groceriesList.add(item2);
        groceriesList.add(item3);
        groceriesList.add(item4);
        groceriesList.add(item5);
        groceriesList.add(item6);
        groceriesList.add(item7);
        groceriesList.add(item8);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Input category of the goods: ");
        Integer search = scanner.nextInt();

        Double lowestPrice = 0.0;
        List<Double> priceCollection = new ArrayList<>();

        for (int i = 0; i < groceriesList.size(); i++) {
            Boolean keyword = groceriesList.get(i).getName().contains("High");
            Boolean categoryOne = groceriesList.get(i).getCategory().equals(1);
            Boolean categoryTwo = groceriesList.get(i).getCategory().equals(2);
            if (keyword && categoryOne
                    || keyword && categoryTwo) {
                priceCollection.add(groceriesList.get(i).getPrice());
            }
        }

        for (int i = 0; i < priceCollection.size(); i++) {
            if (priceCollection.get(i) <= lowestPrice) {
                lowestPrice = priceCollection.get(i);
            }
        }

        System.out.println(groceriesList);
        System.out.println(priceCollection);
        System.out.println("Lowest price of the goods is " + lowestPrice);
    }
}
