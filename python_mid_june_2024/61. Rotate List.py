# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rotate(head):
            prev = head
            tail = head.next
            post = tail.next
            while post:
                prev = tail
                tail = post
                post = tail.next
            prev.next = None
            tail.next = head
            return tail
        
        length = 0
        curr = head
        if not head or not head.next:
            return head
        while curr:
            curr = curr.next
            length += 1
        k %= length
        while k > 0:
            head = rotate(head)
            k -= 1
        return head