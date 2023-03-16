package org.example.seminare2.cw.Store;

import org.example.seminare2.cw.Customer.Customer;

import java.util.*;

public class Market implements QueueBehavior, MarketBehavior {
    List<Customer> customersList = new LinkedList<>();
    Queue<Customer> customersQueue = new ArrayDeque<>();
    @Override
    public void acceptToMarket(Customer customer) {
        customersList.add(customer);
    }

    @Override
    public void releaseFromMarket(Customer customer) {
        customersList.remove(customer);
    }

    @Override
    public void update() {

    }

    @Override
    public void takeIdQueue(Customer customer) {
        customersQueue.add(customer);
    }

    @Override
    public void takeOrders() {
        customersQueue.peek().isTakeOrder();
    }

    @Override
    public void giveOrders() {
        customersQueue.peek().isMakeOrder();
    }

    @Override
    public void releaseFromQueue() {
        customersQueue.poll();
    }
}
