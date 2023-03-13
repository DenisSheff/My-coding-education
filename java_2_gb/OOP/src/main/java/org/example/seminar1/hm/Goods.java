package org.example.seminar1.hm;

 abstract class Goods {
    protected static String name;
    protected static int price;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
     @Override
     public String toString() {
         return "Product {" +
                 "name: " + name + '\'' +
                 ", price: " + price + '\'' +
                 "}";
     }
}
