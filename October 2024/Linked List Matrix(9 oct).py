class Node:
    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None

class Solution:
    def constructLinkedMatrix(self, mat):
        n = len(mat)
        
        # Check for empty matrix
        if n == 0 or len(mat[0]) == 0:
            return None
        
        head = Node(mat[0][0])
        node = head
        
        for row in range(n):
            curr = node
            
            for col in range(len(mat[row])):
                if col + 1 < len(mat[row]):
                    curr.right = Node(mat[row][col + 1])
                if row + 1 < n:
                    curr.down = Node(mat[row + 1][col])
                curr = curr.right
            
            if row + 1 < n:
                node = node.down

        return head