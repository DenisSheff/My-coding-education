package org.example.seminar4.cw.task2;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
//        LinkedList<Integer> linkedList = new LinkedList<>();
//        Scanner scanner = new Scanner(System.in);
//        System.out.print("Input a number for the list length: ");
//        int number = scanner.nextInt();
//        for (int i = 0; i < number; i++) {
//            linkedList.add(i);
//        }
//        scanner.close();

//        System.out.println(linkedList.peek());;
//        System.out.println("peek: " + linkedList);
//        System.out.println(linkedList.pop());
//        System.out.println("pop: " + linkedList);
//
//        linkedList.addFirst(9);
//        linkedList.addLast(5);
//        linkedList.add(105);
//        System.out.println(linkedList);
//
//        linkedList.set(2, 13456);
//        System.out.println(linkedList);
//
//        linkedList.contains(4);
//        System.out.println(linkedList);
//
//        linkedList.remove(2);
//        System.out.println(linkedList);

        LinkedList<Integer> list = new LinkedList<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        int sum = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) % 2 == 0) sum += list.get(i);
        }
        System.out.println(sum);
    }
 }
