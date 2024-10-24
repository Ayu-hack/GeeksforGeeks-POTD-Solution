class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def is_sum_tree(self, root):
        if root is None or (root.left is None and root.right is None):
            return 1
            
        def get_sum(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.data
                
            # If we find invalid sum tree, return -1
            left_sum = get_sum(node.left)
            if left_sum == -1:
                return -1
                
            right_sum = get_sum(node.right)
            if right_sum == -1:
                return -1
                
            # Check if current node follows sum tree property
            if node.data != left_sum + right_sum:
                return -1
                
            # Return total sum for this subtree
            return node.data + left_sum + right_sum
            
        return 1 if get_sum(root) != -1 else 0

# Driver Code
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.strip().split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = []

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.pop(0)
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        print(ob.is_sum_tree(root))
