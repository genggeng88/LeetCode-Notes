"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def doubly(root): 
            if not root:
                return None, None
            
            head = root
            tail = root
            if root.left:
                head, tail_left = doubly(root.left)
                tail_left.right = root
                root.left = tail_left
            
            if root.right:
                head_right, tail = doubly(root.right)
                root.right = head_right
                head_right.left = root
            head.left = tail
            tail.right = head
            return (head, tail)

        
        head, tail = doubly(root)
        return head