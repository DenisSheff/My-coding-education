package org.example.seminar6.hw.model.singleton;
import java.io.*;
import java.util.Scanner;
public class Logger {
    private static Logger logger;
    private final File file = new File("log.txt");

    public static Logger getLogger() {
        if (logger == null) {
            logger = new Logger();
        }
        return logger;
    }

    private Logger() {

    }

    public void addLogInfo(String log) {
        try (FileWriter fw = new FileWriter(file, true)) {
            fw.write(log + "\n\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String readLog() {
        StringBuffer sb = new StringBuffer();
        try (FileReader fr = new FileReader(file)) {
            Scanner sc = new Scanner(fr);

            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                sb.append(line).append("\n");

            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sb.toString();
    }
}
