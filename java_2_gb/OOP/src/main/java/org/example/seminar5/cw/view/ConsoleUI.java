package org.example.seminar5.cw.view;
import java.util.Scanner;
public class ConsoleUI {
    public void printMainMenu() {
        String mainMenu = """
                1 - Добавить продукт в торговый автомат;
                2 - Получить продукт из торгового автомата;
                3 - Показать список продуктов;
                Exit - выйти из программы""";
        System.out.println(mainMenu);
    }

    public void printAddMenu() {
        String menuAddDrinkables = """
                1 - Бутилированный напиток;
                2 - Горячий напиток;
                """;
        System.out.println(menuAddDrinkables);
    }

    public void printBottleMenu() {
        String bottleMenu = """
                1 - Поиск по названию;
                2 - Поиск по цене;""";
        System.out.println(bottleMenu);
    }
    public void printHotMenu() {
        String hotMenu = """
                1 - Поиск по названию;
                2 - Поиск по цене;
                3 - Поиск по температуре""";
        System.out.println(hotMenu);
    }
    public String setChoice(String message) {
        System.out.print(message + ": ");
        return new Scanner(System.in).nextLine();
    }
    public void printMessage(String message){
        System.out.println(message);
    }
}
