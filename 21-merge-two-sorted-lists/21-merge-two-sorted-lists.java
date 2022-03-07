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
    private ListNode SortedMerge(ListNode A, ListNode B){
        if(A == null) return B;
        if(B == null) return A;
        if(A.val < B.val)
        {
            A.next = SortedMerge(A.next, B);
            return A;
        }
        B.next = SortedMerge(A, B.next);
        return B;         
    }
    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        return SortedMerge(l1,l2);
    }
}