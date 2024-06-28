# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end) -> Optional[ListNode]:
            marked = curr = start.next
            post = curr.next
            ppost = post.next
            
            while ppost != end:
                post.next = curr
                curr = post
                post = ppost
                ppost = ppost.next

            start.next = post
            post.next = curr
            marked.next = end
            return marked

        if k == 1:
            return head

        dummy = ListNode(0, head)
        start, acc = dummy, 0
        while head:
            acc += 1
            head = head.next
            if acc == k:
                start = reverse(start, head)
                acc = 0
        return dummy.next