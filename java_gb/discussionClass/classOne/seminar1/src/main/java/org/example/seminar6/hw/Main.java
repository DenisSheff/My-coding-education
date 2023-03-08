package org.example.seminar6.hw;

import java.util.*;

public class Main {

    public static void main(String[] args) {

        Set<Laptop> allItems = new HashSet<>();

        Laptop laptop1 = new Laptop("Apple", "MacBook Air",
                8, 256, "Mac OS", "Grey", 13.6, 105000);
        Laptop laptop2 = new Laptop("Apple", "MacBook Pro",
                32, 1000, "Mac OS", "Dark Grey", 16.0, 250000);
        Laptop laptop3 = new Laptop("Apple", "MacBook",
                8, 512, "Mac OS", "Pink", 12.0, 90000);
        Laptop laptop4 = new Laptop("Apple", "MacBook Pro",
                16, 512, "Mac OS", "Grey", 14.1, 200000);
        Laptop laptop5 = new Laptop("Apple", "MacBook Air",
                16, 2000, "Mac OS", "Grey", 13.6, 150000);
        Laptop laptop6 = new Laptop("Samsung", "Galaxy Book",
                8, 256, "Windows", "Black", 14.0, 100000);
        Laptop laptop7 = new Laptop("Samsung", "Galaxy Book Ultra",
                64, 3000, "Windows", "Black", 16.0, 350000);
        Laptop laptop8 = new Laptop("Samsung", "Galaxy Book Pro",
                32, 1000, "Windows", "White", 14.0, 200000);


        allItems.add(laptop1);
        allItems.add(laptop2);
        allItems.add(laptop3);
        allItems.add(laptop4);
        allItems.add(laptop5);
        allItems.add(laptop6);
        allItems.add(laptop7);
        allItems.add(laptop8);

        LaptopCooperations begin = new LaptopCooperations(allItems);
        begin.start();

    }
}
