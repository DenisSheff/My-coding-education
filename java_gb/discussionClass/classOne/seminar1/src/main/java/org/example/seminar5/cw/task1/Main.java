package org.example.seminar5.cw.task1;

import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        HashMap<Character, Integer> myMap = new HashMap<>();
        String str = "qwer qwerty qaz wsx rfv tgb qaz rfv  tghbn ujm";
        for (int i = 0; i < str.length(); i++) {
            myMap.putIfAbsent(str.charAt(i), 0);
            myMap.put(str.charAt(i), myMap.get(str.charAt(i)) + 1);
//            if (!myMap.containsKey(str.charAt(i))) {
//                myMap.put(str.charAt(i), 1);
//            } else {
//                myMap.put(str.charAt(i), myMap.get(str.charAt(i)) + 1);
//            }
        }
        for (Map.Entry<Character, Integer> entry : myMap.entrySet()) {
            System.out.println(entry.getKey() + " entrance " + entry.getValue());
        }
    }
}
