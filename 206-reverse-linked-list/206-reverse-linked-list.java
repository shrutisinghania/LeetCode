/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rev(ListNode l, ListNode head)
    {
        if(head == null)
            return l;
        ListNode p = new ListNode(head.val, l);
        return rev(p, head.next);
        
    }
    public ListNode reverseList(ListNode head) {
        return rev(null, head);
    }
}