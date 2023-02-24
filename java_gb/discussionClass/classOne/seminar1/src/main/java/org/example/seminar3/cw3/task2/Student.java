package org.example.seminar3.cw3.task2;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.ArrayList;
import java.util.List;

@Data
@AllArgsConstructor
public class Student {
    private String lastName;
    private String groupNumber;
    private Integer scholarship;
    List<Integer> grade;
}
