package org.example.seminar6.cw.task3;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> list1 = new ArrayList<>(Arrays.asList("qwe", "asd", "x"));
        ArrayList<String> list2 = new ArrayList<>(Arrays.asList("v"));
        Map<String, Integer> mapList = new HashMap<>();
        for (int i = 0; i < list1.size(); i++) {
            mapList.putIfAbsent(list1.get(i), 0);
            mapList.put(list1.get(i), mapList.get(list1.get(i)) + 1);
        }for (int i = 0; i < list2.size(); i++) {
            mapList.putIfAbsent(list2.get(i), 0);
            mapList.put(list2.get(i), mapList.get(list2.get(i)) + 1);
        }
        Set<String> setList = new HashSet<>(list1);
        setList.retainAll(new HashSet<>(list2));
        if (setList.size() > 0) {
            for (String el : setList) {
                System.out.printf("%s = %d\n", el, mapList.get(el));
            }
        }
        else {
            System.out.println("There is no intersection.");
        }
    }
}
