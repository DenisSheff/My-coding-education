package org.example.seminar1.hw1;

//Given an input string s, reverse the order of the words.
//A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
//Return a string of the words in reverse order concatenated by a single space.
//Note that s may contain leading or trailing spaces or multiple spaces between two words.
//The returned string should only have a single space separating the words. Do not include any extra spaces.
//Input: s = "the sky is blue"
//Output: "blue is sky the"

import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String myString = scanner.nextLine();
        StringBuilder newString = new StringBuilder();
        newString
                .append(myString.substring(myString.length() / 2, myString.length()))
                .append(myString.substring(0, myString.length() / 2));
        System.out.println(newString);
    }
}
