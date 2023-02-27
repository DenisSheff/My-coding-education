package org.example.seminar3.hw3.task2;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class NewItem {
    private String goodsName;
    private String countryName;
    private Double weight;
    private Double price;
    private Integer category;
}
