package org.example.seminar3.cw3.task3;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Box box = new Box(3, "black", "wood");
        Box box1 = new Box(5, "white", "metal");
        Box box2 = new Box(2, "yellow", "cardboard");
        Box box3 = new Box(3, "yellow", "wood");
        Box box4 = new Box(3, "green", "cardboard");
        Box box5 = new Box(1, "black", "wood");
        Box box6 = new Box(15, "yellow", "metal");
        Box box7 = new Box(20, "yellow", "cardboard");
        Box box8 = new Box(10, "blue", "cardboard");
        Box box9 = new Box(7, "red", "metal");
        Box box10 = new Box(3, "brown", "wood");

        List<Box> boxCollection = new ArrayList<>();
        boxCollection.add(box);
        boxCollection.add(box1);
        boxCollection.add(box2);
        boxCollection.add(box3);
        boxCollection.add(box4);
        boxCollection.add(box5);
        boxCollection.add(box6);
        boxCollection.add(box7);
        boxCollection.add(box8);
        boxCollection.add(box9);
        boxCollection.add(box10);
        System.out.println(boxCollection);

        Integer colorCounter = 0;
        Integer capacity = 0;
        Integer woodenBox = 0;

        for (int i = 0; i < boxCollection.size(); i++) {
            if (boxCollection.get(i).getColor().equals("yellow")) {
                colorCounter++;
                capacity += capacityBox(boxCollection.get(i).getSide());
            }
            if (boxCollection.get(i).getMaterial().equals("wood") && boxCollection.get(i).getSide() == 3) {
                woodenBox++;
            }
        }
        System.out.println(colorCounter);
        System.out.println(capacity);
        System.out.println(woodenBox);
    }

    private static Integer capacityBox(Integer side) {
        return (int) Math.pow(side, 3);
    }
}
