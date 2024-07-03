# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwo(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            
            dummy_head = ListNode(0, list2)
            dummy, head1, head2 = dummy_head, list1, list2

            while head1 and head2:
                if head1.val > head2.val:
                    head2 = head2.next
                    dummy = dummy.next
                else:
                    tmp = head1.next
                    dummy.next = head1
                    head1.next = head2
                    dummy = head1
                    head1 = tmp
                    
            if not head2:
                dummy.next = head1
            return dummy_head.next

        if not lists:
            return None
        
        res = lists[0]
        for i in range(1, len(lists)):
            res = mergeTwo(res, lists[i])
        
        return res