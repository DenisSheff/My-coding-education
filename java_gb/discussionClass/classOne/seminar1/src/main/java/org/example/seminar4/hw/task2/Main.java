package org.example.seminar4.hw.task2;

public class Main {
    public static void main(String[] args) {
        System.out.println(ValidParentheses.isValid("()"));
        System.out.println(ValidParentheses.isValid("{}"));
        System.out.println(ValidParentheses.isValid("[]"));
        System.out.println(ValidParentheses.isValid("("));
        System.out.println(ValidParentheses.isValid(")"));
        System.out.println(ValidParentheses.isValid("{]"));
        System.out.println(ValidParentheses.isValid(")("));
        System.out.println(ValidParentheses.isValid("]["));
        System.out.println(ValidParentheses.isValid("}{"));
    }
}
