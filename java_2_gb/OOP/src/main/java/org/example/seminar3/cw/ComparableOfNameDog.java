package org.example.seminar3.cw;

import java.util.Comparator;

public class ComparableOfNameDog implements Comparator<Dog> {

    @Override
    public int compare(Dog o1, Dog o2) {
        return o1.getName().compareTo(o2.getName());
    }
}
