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
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode curr = head, post = head.next;
        curr.next = null;
        while (post != null) {
            ListNode tmp = post.next;
            post.next = curr;
            curr = post;
            post = tmp;
        }
        return curr;
    }
}