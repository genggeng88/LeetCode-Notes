"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connectHelper(node):
            if not node:
                return 

            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = findNext(node.next)
            if node.right:
                node.right.next = findNext(node.next)

            connectHelper(node.right)
            connectHelper(node.left)
            

        def findNext(node):
            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                node = node.next
            return None
        
        if not root:
            return root

        connectHelper(root)
        return root