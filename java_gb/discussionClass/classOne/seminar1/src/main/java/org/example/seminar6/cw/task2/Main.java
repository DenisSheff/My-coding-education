package org.example.seminar6.cw.task2;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Set<Integer> set1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        Set<Integer> set2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8));
        Set<Integer> tempSet = new HashSet<>(set1);
        tempSet.retainAll(set2);
        System.out.println(set1);
        System.out.println(set2);
        System.out.println(tempSet);
    }
}
