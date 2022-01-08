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
    public int pairSum(ListNode head) {
        ListNode a = head;
        ArrayList<Integer> arr = new ArrayList<Integer>();
        while(a!=null)
        {
            arr.add(a.val);
            a = a.next;
        }
        int n = arr.size();
        int max=arr.get(0);
        for(int i =0; i < n/2; ++i)
            max = Math.max(max, arr.get(i) + arr.get(n-1-i));
        return max;
    }
}