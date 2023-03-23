package org.example.seminar3.cw;

import java.util.Iterator;
import java.util.List;

public class ListOfDogsIterator implements Iterator<Dog> {
    private List<Dog> listOfDogIterable;
    public static int counter;
    public ListOfDogsIterator(List<Dog> listOfDogIterable) {
        this.listOfDogIterable = listOfDogIterable;
        counter = 0;
    }

    @Override
    public boolean hasNext() {
        return counter < listOfDogIterable.size() - 1;
    }

    @Override
    public Dog next() {
        if (!hasNext()) return null;
        counter++;
        return listOfDogIterable.get(counter);
    }
}
