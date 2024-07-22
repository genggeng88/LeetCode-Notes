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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int cnt = 0;
        ListNode tmp = head;
        while (tmp != null) {
            cnt++;
            tmp = tmp.next;
        }
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        ListNode curr = head;
        ListNode post = curr.next;
        int idx = 0;
        while (idx <= cnt - n) {
            if (idx == cnt - n) {
                prev.next = post;
                return dummy.next;
            }
            prev = curr;
            curr = post;
            post = post.next;
            idx++;
        }
        return dummy.next;
    }
}