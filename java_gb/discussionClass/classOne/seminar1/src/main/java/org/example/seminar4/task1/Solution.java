package org.example.seminar4.task1;

public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode previous = null;
        ListNode current = head;
        while (current != null) {
            ListNode nextEl = current.next;
            current.next = previous;
            previous = current;
            current = nextEl;
        }
        return previous;
    }
}
