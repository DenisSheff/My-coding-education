package org.example.seminar5.hw.task1;

import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        String text = "Россия идет позади всей планеты. Планета — это не Россия.";
        String [] arr = text.split(" ");
        Map<String, Integer> mapList = new HashMap<>();
        for (String word : arr) {
            String wordInArr = word.toLowerCase();
            if (mapList.containsKey(wordInArr)) {
                mapList.replace(wordInArr, mapList.get(wordInArr), mapList.get(wordInArr).intValue() + 1);
            } else {
                mapList.put(wordInArr, 1);
            }
        }
        for (Map.Entry<String, Integer> entry : mapList.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
     }
}
