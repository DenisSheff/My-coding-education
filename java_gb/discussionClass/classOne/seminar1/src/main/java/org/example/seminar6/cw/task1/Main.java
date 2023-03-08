package org.example.seminar6.cw.task1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 3, 2, 1, 5));
        Set<Integer> setList = new HashSet<>(list);
        System.out.printf("Percentage of unique numbers: %d", setList.size() * 100 / list.size());
    }
}
