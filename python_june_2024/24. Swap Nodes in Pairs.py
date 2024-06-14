# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        if not head.next.next:
            tmp = head.next
            tmp.next = head
            head.next = None
            return tmp
        tmp = head.next
        post = tmp.next
        tmp.next = head
        head.next = self.swapPairs(post)
        return tmp