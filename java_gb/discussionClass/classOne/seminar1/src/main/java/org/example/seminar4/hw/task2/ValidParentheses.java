package org.example.seminar4.hw.task2;

import java.util.LinkedList;

public class ValidParentheses {
    public static boolean isValid(String s) {
        LinkedList<Character> parenthesesList = new LinkedList<>();
        for (char i : s.toCharArray()) {
            if (i == '(' || i == '[' || i == '{') {
                parenthesesList.addFirst(i);
            } else {
                if (parenthesesList.isEmpty() || (i == ')' && parenthesesList.peek() != '(')
                        || (i == '}' && parenthesesList.peek() != '{')
                        || (i == ']' && parenthesesList.peek() != '[')) {
                    return false;
                }
                parenthesesList.pop();
            }
        }
        return parenthesesList.isEmpty();
    }
}
