package org.example.seminar4.task5;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class Solution {
    public static void main(String[] args) {
        String text = "/../";
        System.out.println(simplifyPath(text));
    }
    public static String simplifyPath(String path) {
        Deque<String> list = new LinkedList<>();
        String[] array = path.split("/");
        for (int i = 0; i < array.length; i++) {
            if (array[i].equals("") || array[i].equals(".")) {
                continue;
            }
            else if (array[i].equals("..")) {
                if (!list.isEmpty())
                {
                    list.pollLast();
                }
            }
            else {
                list.add(array[i]);
            }
        }
        return "/" + String.join("/", list);
    }
}
