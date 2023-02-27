package org.example.seminar4.task3;

import java.util.Arrays;
import java.util.LinkedList;


//Заменить некратные 3 элементы списка, суммой нечетных элементов.
public class Main {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        int sum = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) % 2 != 0) {
                sum += list.get(i);
            }
        }
        System.out.println(list);
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) % 3 != 0) {
                list.set(i, sum);
            }
        }
        System.out.println(list);
     }
}
