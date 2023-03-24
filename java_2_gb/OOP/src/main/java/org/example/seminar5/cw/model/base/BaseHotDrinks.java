package org.example.seminar5.cw.model.base;
import org.example.seminar5.cw.model.HotDrinks;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;
public class BaseHotDrinks {
    private List<HotDrinks> list;

    public BaseHotDrinks() {
        this.list = importList();
    }
    private List<HotDrinks> importList() {
        List<HotDrinks> listOfHot = new ArrayList<>();
        File file = new File("baseHotDrinks.txt");
        try (FileReader reader = new FileReader(file)) {
            BufferedReader reader1 = new BufferedReader(reader);
            String line = reader1.readLine();
            while (line != null) {
                String[] lineArray = line.split(";");
                listOfHot.add(new HotDrinks(
                        lineArray[0],
                        Float.parseFloat(lineArray[1]),
                        Double.parseDouble(lineArray[2]),
                        Integer.parseInt(lineArray[3])));
                line = reader1.readLine();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return listOfHot;
    }
    public void addAtBase(String name, float price, double value, int temperature) {
        this.list.add(new HotDrinks(name, price, value, temperature));
    }
    public void exportBase() {
        File file = new File("baseHotDrinks.txt");
        try (FileWriter writer = new FileWriter(file)) {
            for (HotDrinks el : this.list) {
                writer.write(
                        el.getName() + ";" +
                                el.getPrice() + ";" +
                                el.getVolume() + ";" +
                                el.getTemp() + "\n");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public List<HotDrinks> getList() {
        return list;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (HotDrinks el : list) {
            builder.append(el.toString()).append("\n");
        }
        return builder.toString();
    }

}
