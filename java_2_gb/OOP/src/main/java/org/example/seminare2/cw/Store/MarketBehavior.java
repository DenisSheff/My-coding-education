package org.example.seminare2.cw.Store;

import org.example.seminare2.cw.Customer.Customer;

import java.util.List;

public interface MarketBehavior {
    void acceptToMarket(Customer customer);
    void releaseFromMarket(Customer customer);
    void update();
}
