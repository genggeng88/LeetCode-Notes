# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        acc, curr = 1, head
        if left == 1:
            subHead = None
        else:
            while curr:
                if acc == left - 1:
                    subHead = curr
                curr = curr.next
                acc += 1
                if acc == left:
                    break
        
        tail = prev = curr
        mid = prev.next
        
        while acc < right:
            post = mid.next
            mid.next = prev
            acc += 1
            prev = mid
            mid = post

        if not subHead:
            head = prev
        else:
            subHead.next = prev
        
        tail.next = mid
        return head