# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_val(head: Optional[ListNode]) -> int:
            acc = 0
            ans = 0
            while head:
                ans += 10**acc*head.val
                head = head.next
                acc += 1
            return ans
        
        def get_tree(num):
            if num == 0:
                return ListNode(0)

            head = ListNode(num % 10)
            curr = head
            num //= 10
            while num > 0:
                curr.next = ListNode(num % 10)
                curr = curr.next
                num //= 10
            return head
        
        n1 = get_val(l1)
        n2 = get_val(l2)
        return get_tree(n1+n2)
