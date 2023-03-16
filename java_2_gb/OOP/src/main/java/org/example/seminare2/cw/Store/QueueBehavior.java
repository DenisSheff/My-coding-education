package org.example.seminare2.cw.Store;

import org.example.seminare2.cw.Customer.Customer;

public interface QueueBehavior {
    void takeIdQueue(Customer customer);
    void takeOrders();
    void giveOrders();
    void releaseFromQueue();
}
