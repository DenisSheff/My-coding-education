package org.example.seminar3.cw;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ListOfDogs listDogs = new ListOfDogs();
        listDogs.setListDogs(Arrays.asList(
                new Dog("Johny", 10, "Black"),
                new Dog("Anthony", 1, "Brown"),
                new Dog("Barbara", 5, "Red")));
        Iterator<Dog> iter = listDogs.iterator();
        while (iter.hasNext()){
            System.out.println(iter.next());
        }
        listDogs.getListDogs().sort(new ComparableOfNameDog());
        for (Dog dog: listDogs){
            System.out.println(dog);
        }
    }
}
