package org.example.seminar1.cw1;

//Дан массив целых чисел. Верно ли, что массив является симметричным.
public class Task5 {
    public static void main(String[] args) {
        int[] myArray = {1, 2, 3, 6, 3, 3, 1};
        System.out.println(test(myArray));

    }
    public static String test(int[] array) {
        boolean flag = true;
        for (int i = 0; i < array.length / 2; i++) {
            if (array[i] != array[array .length - 1 - i]) {
               return ("The block is asymmetric.");
            }
        }
        return ("The block is symmetric.");
    }
}
