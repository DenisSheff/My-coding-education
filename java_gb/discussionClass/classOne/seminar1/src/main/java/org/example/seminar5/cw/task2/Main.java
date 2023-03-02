package org.example.seminar5.cw.task2;

import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 1, 2};
        System.out.println(isDouble(array));
    }

    public static boolean isDouble(int[] block) {
        Map<Integer, Integer> mapList = new HashMap<>();
        for (int i = 0; i < block.length; i++) {
            if (mapList.containsKey(block[i])) {
                return true;
            } else {
                mapList.put(block[i], 1);
            }
        }
         return false;
    }
}
