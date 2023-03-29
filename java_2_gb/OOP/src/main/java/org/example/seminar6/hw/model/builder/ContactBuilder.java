package org.example.seminar6.hw.model.builder;

public class ContactBuilder {
    private String surname;
    private String name;
    private String patronymic;
    private String phone;
    private String email;
    private String address;

    public ContactBuilder surname(String surname) {
        this.surname = surname;
        return this;
    }

    public ContactBuilder name(String name) {
        this.name = name;
        return this;
    }

    public ContactBuilder patronymic(String patronymic) {
        this.patronymic = patronymic;
        return this;
    }

    public ContactBuilder phone(String phone) {
        this.phone = phone;
        return this;
    }

    public ContactBuilder email(String email) {
        this.email = email;
        return this;
    }

    public ContactBuilder address(String address) {
        this.address = address;
        return this;
    }

    public String getSurname() {
        return surname;
    }

    public String getName() {
        return name;
    }

    public String getPatronymic() {
        return patronymic;
    }

    public String getPhone() {
        return phone;
    }

    public String getEmail() {
        return email;
    }

    public String getAddress() {
        return address;
    }

    public Contact build() {
        return new Contact(this);
    }
}
