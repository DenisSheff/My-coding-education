package org.example.seminar3.cw3.task2;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Student student1 = new Student("Abramov", "535OM", 0, List.of(4, 2, 3));
        Student student2 = new Student("Ivanova", "530OM", 3000, List.of(4, 4, 4));
        Student student3 = new Student("Sidorov", "535OM", 5000, List.of(5, 5, 5));
        Student student4 = new Student("Petrova", "545OM", 0, List.of(2, 2, 3));
        Student student5 = new Student("Gnomova", "535OM", 1000, List.of(5, 2, 3));

        List<Student> allStudents = new ArrayList<>();
        allStudents.add(student1);
        allStudents.add(student2);
        allStudents.add(student3);
        allStudents.add(student4);
        allStudents.add(student5);

        for (Student student : allStudents) {
            if (searchLastNameEnd(student.getLastName(), "ova")) {
                int sum = 0;
                for (Integer grade : student.getGrade()) {
                    sum += grade;
                }
                if (sum % 2 == 0) {
                    System.out.println("Student = " + student.getLastName());
                    System.out.println("Scholarship = " + student.getScholarship());
                }
            }
        }
    }

    public static boolean searchLastNameEnd(String name, String searching) {
        int charCount = name.length() - searching.length();
        if (name.substring(charCount).equals(searching)) return true;
        return false;
    }
}
