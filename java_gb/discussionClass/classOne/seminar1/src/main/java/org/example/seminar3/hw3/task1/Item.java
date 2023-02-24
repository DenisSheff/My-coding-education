package org.example.seminar3.hw3.task1;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Item {
    private String name;
    private Double price;
    private Integer category;
}
