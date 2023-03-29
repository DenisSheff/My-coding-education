package org.example.seminar6.hw.service;

import org.example.seminar6.hw.model.builder.Contact;
import org.example.seminar6.hw.model.builder.ContactBuilder;
import org.example.seminar6.hw.model.singleton.Logger;
import org.example.seminar6.hw.ui.UIConsole;

public class Service {
    UIConsole console = new UIConsole();

    public void start() {
        console.printMessage("Старт программы.\n");
        Contact contact1 = new ContactBuilder()
                .name("Алеша")
                .surname("Попович")
                .phone("911")
                .email("Popa@mail.ru")
                .patronymic("Леонтьевич")
                .address("не сказал")
                .build();
        Logger.getLogger().addLogInfo("Создана запись\n" + contact1);
        Contact contact2 = new ContactBuilder()
                .surname("Муромец")
                .name("Илья")
                .address("Печь")
                .build();
        Logger.getLogger().addLogInfo("Создана запись\n" + contact2);
        console.printMessage(Logger.getLogger().readLog());
        console.printMessage("Работа программы завершена");
    }
}
