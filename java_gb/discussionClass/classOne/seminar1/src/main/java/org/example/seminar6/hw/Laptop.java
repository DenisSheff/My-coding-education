package org.example.seminar6.hw;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.*;

@Data
@AllArgsConstructor

public class Laptop {
    private String laptopBrand;
    private String laptopName;
    private Integer laptopRAM;
    private Integer laptopSSD; //MB
    private String laptopOS;
    private String laptopColor;
    private Double screenSize;
    private Integer laptopPrice; //Roubles


    @Override
    public String toString() {
        return "Laptop by: (" + laptopBrand + "): " +
                ", model: " + laptopName +
                ", RAM:" + laptopRAM +
                ", amount of SSD: " + laptopSSD +
                ", OS: " + laptopOS + '\'' +
                ", color: " + laptopColor +
                ", screen size: " + screenSize +
                ", price: " + laptopPrice + "\n";
    }

    public class LaptopCooperations {
        private Set<Laptop> laptopsList = new HashSet<>();
        private List<Options> optionsList = new ArrayList<>();
        private static Scanner scanner = new Scanner(System.in);


        public void printList(){
            for (Laptop laptop : laptopsList){
                if (notebookIsCorrect(laptop)){
                    System.out.println(laptop);
                }
            }
        }

        public boolean notebookIsCorrect(Laptop laptop){

            for (Options option : optionsList){
                Object laptopValue = null;

                if (option.property.equals("laptopBrand")){
                    laptopValue = laptop.getLaptopBrand();
                }else if (option.property.equals("laptopName")){
                    laptopValue = laptop.getLaptopName();
                }else if (option.property.equals("laptopRAM")){
                    laptopValue = laptop.getLaptopRAM();
                }else if (option.property.equals("laptopSSD")) {
                    laptopValue = laptop.getLaptopSSD();
                } else if (option.property.equals("laptopOS")){
                    laptopValue = laptop.getLaptopOS();
                } else if (option.property.equals("laptopColor")) {
                    laptopValue = laptop.getLaptopColor();
                } else if (option.property.equals("screenSize")) {
                    laptopValue = laptop.getScreenSize();
                } else if (option.property.equals("laptopPrice")) {
                    laptopValue = laptop.getLaptopPrice();
                } else {
                    continue;
                }

                if (option.value != null && !option.value.equals(laptopValue)){
                    return false;
                }

                if (option.maxValue != null && option.maxValue < Double.parseDouble(Objects.toString(laptopValue))){
                    return false;
                }

                if (option.minValue != null && option.minValue > Double.parseDouble(Objects.toString(laptopValue))){
                    return false;
                }
            }
            return true;
        }

        public LaptopCooperations(Set<Laptop> notebooks) {
            this.scanner = new Scanner(System.in);
            this.laptopsList = notebooks;
        }

        public String getOptionsDescriptions(String property) {

            Map<String, String> optionsDescriptions = describeOptions();

            return optionsDescriptions.get(property);

        }
        public Map<String, String> describeOptions() {
            Map<String, String> mapList = new HashMap<>();

            mapList.put("laptopBrand", "Brand name");
            mapList.put("laptopName", "Laptop name");
            mapList.put("laptopRAM", "Amount of RAM");
            mapList.put("laptopSSD", "Amount of disk memory");
            mapList.put("laptopOS", "Laptop operation system");
            mapList.put("laptopColor", "Laptop color");
            mapList.put("laptopSize", "Laptop screen size");
            mapList.put("laptopPrice", "Laptop price");

            return mapList;
        }
        public List<String> filterTechSpecs(){
            List<String> list = new ArrayList<>();
            list.add("laptopBrand");
            list.add("laptopName");
            list.add("laptopRAM");
            list.add("laptopSSD");
            list.add("laptopOS");
            list.add("laptopColor");
            list.add("laptopSize");
            list.add("laptopPrice");
            return list;
        }

        public String getListOfOptions(){
            String text = "Here is a menu: \n " +
                    "1. Show all \n " +
                    "2. Sort \n " +
                    "3. Exit\n" +
                    "Choose your option: ";

            System.out.print(text);
            String answer = scanner.next();
            return answer;
        }

        public Set<String> selectAmount() {
            Set<String> setList = new HashSet<>();

            setList.add("laptopRAM");
            setList.add("laptopSSD");
            setList.add("laptopSize");
            setList.add("laptopPrice");

            return setList;
        }

        public Set<String> select() {
            Set<String> setList = new HashSet<>();

            setList.add("laptopBrand");
            setList.add("laptopName");
            setList.add("laptopOS");
            setList.add("laptopColor");

            return setList;
        }

        public String showOptions() {
            String text = "---------------------------\n" +
                    "What would you like to choose?:\n" +
                    "1. Brand\n" +
                    "2. Laptop name\n" +
                    "3. RAM amount\n" +
                    "4. SSD amount\n" +
                    "5. OS\n" +
                    "6. Color\n" +
                    "7. Screen size\n" +
                    "8. Price\n" +
                    "Choose your option: ";

            System.out.print(text);
            String answer = scanner.next();
            return answer;
        }

        public void start(){
            Set<Laptop> block = new HashSet<>();
            boolean flag = true;
            while (flag){
                String operation = getListOfOptions();
                if (operation.equals("3")) {
                    flag = false;
                    scanner.close();
                } else if (operation.equals("1")) {
                    printList();
                }
                else if (operation.equals("2")){
                    String nextAction = showOptions();
                    if (nextAction.equals("1")) {

                    }
                }
            }
        }


    }

}
