package org.example.seminar3.cw3.task4;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Box box = new Box(3, "black", "wood");
        Box box1 = new Box(5, "white", "metal");
        Box box2 = new Box(3, "yellow", "wood");
        Box box3 = new Box(3, "yellow", "wood");

        List<Box> boxCollection = new ArrayList<>();
        boxCollection.add(box);
        boxCollection.add(box1);
        boxCollection.add(box2);
        boxCollection.add(box3);
        System.out.println(boxCollection);
        System.out.println("Unique List: " + isUniqueCollection(boxCollection));

    }

    private static Collection isUniqueCollection(List<Box> boxCollection) {
        return new HashSet(boxCollection);
    }

    private static Integer capacityBox(Integer side) {
        return (int) Math.pow(side, 3);
    }
}
