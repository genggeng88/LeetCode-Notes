# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        tmp = head.next
        head.next = None

        while tmp.next:
            post = tmp.next
            tmp.next = head
            head = tmp
            tmp = post
        tmp.next = head
        return tmp
        