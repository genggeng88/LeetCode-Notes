"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def isLeaf(x, y, length):
            val = grid[x][y]
            for i in range(x, x+length):
                for j in range(y, y+length):
                    if grid[i][j] != val:
                        return False, None
            return True, val
        
        def helper(x, y, length):
            left, val = isLeaf(x, y, length)
            if left:
                return Node(val, True)

            half = length//2
            return Node(1, False,
                        helper(x, y, half),
                        helper(x, y+half, half),
                        helper(x+half, y, half),
                        helper(x+half, y+half, half))
        
        return helper(0, 0, n)