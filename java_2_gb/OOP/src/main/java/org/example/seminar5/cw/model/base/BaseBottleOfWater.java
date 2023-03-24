package org.example.seminar5.cw.model.base;


import org.example.seminar5.cw.model.BottleOfWater;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;
public class BaseBottleOfWater {
    private List<BottleOfWater> list;

    public BaseBottleOfWater() {
        this.list = importList();
    }
    private List<BottleOfWater> importList() {
        List<BottleOfWater> listOfBottle = new ArrayList<>();
        File file = new File("baseBottleOfWatter.txt");
        try (FileReader reader = new FileReader(file)) {
            BufferedReader reader1 = new BufferedReader(reader);
            String line = reader1.readLine();
            while (line != null) {
                String[] lineArray = line.split(";");
                listOfBottle.add(new BottleOfWater(
                        lineArray[0],
                        Float.parseFloat(lineArray[1]),
                        Double.parseDouble(lineArray[2])));
                line = reader1.readLine();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return listOfBottle;
    }
    public void addAtBase(String name, float price, double value) {
        this.list.add(new BottleOfWater(name, price, value));
    }


    public void exportBase() {
        File file = new File("baseBottleOfWatter.txt");
        try (FileWriter writer = new FileWriter(file)) {
            for (BottleOfWater el : this.list) {
                writer.write(el.getName() + ";" + el.getPrice() + ";" + el.getVolume() + "\n");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public List<BottleOfWater> getList() {
        return list;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (BottleOfWater el : list) {
            builder.append(el.toString()).append("\n");
        }
        return builder.toString();
    }
}
