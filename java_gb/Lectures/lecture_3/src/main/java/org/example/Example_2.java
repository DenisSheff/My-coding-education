package org.example;

public class Example_2 {
    public static void main(String[] args) {
        System.out.println(Sum(1, 2));
        System.out.println(Sum(1.0, 2));
        System.out.println(Sum(1, 2.0));
        System.out.println(Sum(1.2, 2.1));
    }
    static Object Sum(Object a, Object b) {
        if (a instanceof Double && b instanceof Double) {
            return (Object)((Double) a + (Double) b);
        } else if (a instanceof Integer && b instanceof Integer) {
            return (Object)((Integer) a + (Integer) b);
        } else return 0;
    }
}
