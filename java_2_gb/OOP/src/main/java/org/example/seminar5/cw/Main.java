package org.example.seminar5.cw;


import org.example.seminar5.cw.service.UserServiceImpl;

public class Main {
    public static void main(String[] args) {
        UserServiceImpl userService = new UserServiceImpl();
        userService.start();
    }
}
