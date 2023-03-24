package org.example.seminar5.cw.model;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class VendingMachineAllProducts<T extends Product> implements VendingMachine {
    private List<T> product;
    private final List<T> resultFind = new ArrayList<>();
    public void initProduct(List<T> product) {
        this.product = product;
    }
    public String getProduct(String name) {
        for (T product : product) {
            if (product.getName().equals(name)) return product.toString();
        }
        return "Не найдено!";
    }
    public String getProduct(BigDecimal price) {
        resultFind.clear();
        for (T el : product) {
            if (el.getPrice().compareTo(price) <= 0) resultFind.add(el);
        }
        return resultFind.isEmpty() ? "Не найдено!" : resultFind.toString();
    }
    public String getProduct(int temp) {
        resultFind.clear();
        for (T el : product) {
            if (el instanceof HotDrinks && ((HotDrinks) el).getTemp() <= temp) resultFind.add(el);
        }

        return resultFind.isEmpty() ? "Не найдено!" : resultFind.toString();
    }
    @Override
    public void initProduct() {
    }
    @Override
    public String getProduct() {
        return null;
    }
}
