package org.example.seminar3.hw3.task2;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        NewItem item1 = new NewItem("Chicken", "Сhina", 2.5,150.90, 2);
        NewItem item2 = new NewItem("Pork", "Russia", 1.5,350.90, 5);
        NewItem item3 = new NewItem("Fish", "USA", 10.0,20000.0, 1);
        NewItem item4 = new NewItem("Shrimps", "Mexico", 2.5,170.90, 3);
        NewItem item5 = new NewItem("Beef", "Germany", 7.5,15000.0, 1);


        List<NewItem> newGroceriesList = new ArrayList<>();
        newGroceriesList.add(item1);
        newGroceriesList.add(item2);
        newGroceriesList.add(item3);
        newGroceriesList.add(item4);
        newGroceriesList.add(item5);


        Scanner scanner = new Scanner(System.in);
        System.out.print("Input category of the goods: ");
        String chosenCategory = scanner.nextLine();

        List<Double> priceCollection = new ArrayList<>();

        for (int i = 0; i < newGroceriesList.size(); i++) {
            Boolean search = newGroceriesList.get(i).getCategory().equals(chosenCategory);
            if (search) {
                priceCollection.add(newGroceriesList.get(i).getPrice());
            }
        }
        System.out.println(newGroceriesList);
        System.out.println("Prices of chosen category: " + priceCollection);
//
//        Double lowestPrice = 0.0;
//        List<Double> priceCollection = new ArrayList<>();
//
//        for (int i = 0; i < groceriesList.size(); i++) {
//            Boolean keyword = groceriesList.get(i).getName().contains("High");
//            Boolean categoryOne = groceriesList.get(i).getCategory().equals(1);
//            Boolean categoryTwo = groceriesList.get(i).getCategory().equals(2);
//            if (keyword && categoryOne
//                    || keyword && categoryTwo) {
//                priceCollection.add(groceriesList.get(i).getPrice());
//            }
//        }
//
//        for (int i = 0; i < priceCollection.size(); i++) {
//            if (priceCollection.get(i) <= lowestPrice) {
//                lowestPrice = priceCollection.get(i);
//            }
//        }
//
//        System.out.println(groceriesList);
//        System.out.println(priceCollection);
//        System.out.println("Lowest price of the goods is " + lowestPrice);
    }
}
