package org.example.seminare2.cw;

import org.example.seminare2.cw.Customer.Human;
import org.example.seminare2.cw.Store.Market;

public class Main {
    public static void main(String[] args) {
        Human human = new Human();
        Market market = new Market();
        market.acceptToMarket(human);
        market.takeIdQueue(human);
        market.giveOrders();
        market.takeOrders();
        market.releaseFromQueue();
        market.releaseFromMarket(human);
    }
}
