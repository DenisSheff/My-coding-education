package org.example.seminar4.task4;

import java.util.Arrays;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
//        Построить однонаправленный список целых чисел.  Удалить отрицательные элементы списка.
        LinkedList<Integer> list = new LinkedList<>(Arrays.asList(-2, -3, -4, -5, -8, -6, 7));
//        for (int i = 0; i < list.size(); i++) {
//            if (list.get(i) < 0) list.remove(i);
//        }
//        System.out.println(list);
        for (int i = list.size() - 1 ; i >= 0; i--) {
            if (list.get(i) < 0) list.remove(i);
        }
        System.out.println(list);
    }
}
