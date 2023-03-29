package org.example.seminar6.hw.model.builder;

public class Contact {
    private final String surname;
    private final String name;
    private final String patronymic;
    private final String phone;
    private final String email;
    private final String address;

    protected Contact(ContactBuilder builder) {
        this.surname = builder.getSurname();
        this.name = builder.getName();
        this.patronymic = builder.getPatronymic();
        this.phone = builder.getPhone();
        this.email = builder.getEmail();
        this.address = builder.getAddress();
    }

    @Override
    public String toString() {
        return String.format("Контакт: %s %s %s%nтелефон: %s%nemail: %s%nадрес: %s",
                surname,
                name,
                patronymic,
                phone,
                email,
                address);
    }
}
