package org.example.seminar6.hw;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.Scanner;

@Data
@AllArgsConstructor
public class Options {
    Object value;
    Double minValue;
    Double maxValue;
    boolean isAmount;
    String property;

    public Options(String property, boolean isAmount, Object value, Double minValue, Double maxValue) {
        this.property = property;
        this.isAmount = isAmount;
        this.value = value;
        this.minValue = minValue;
        this.maxValue = maxValue;
    }


}

