"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneNode(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if node:
            if node not in self.visited:
                self.visited[node] = Node(node.val, None, None)
            return self.visited[node]
        
        return None

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_node = head
        new_node = Node(head.val, None, None)
        self.visited[old_node] = new_node

        while old_node:
            
            new_node.next = self.cloneNode(old_node.next)
            new_node.random = self.cloneNode(old_node.random)

            old_node = old_node.next
            new_node = new_node.next
        
        return self.visited[head]
        