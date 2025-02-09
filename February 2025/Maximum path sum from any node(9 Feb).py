class Solution:
    def findMaxSum(self, root):
        def getMaxPathSum(node):
            nonlocal maxSum  # Use nonlocal to modify maxSum inside the nested function
            if not node:
                return 0  # Base case: If node is null, return 0
            
            # Recursively get the maximum sum from left and right subtrees
            leftMax = max(0, getMaxPathSum(node.left))  # Ignore negative sums
            rightMax = max(0, getMaxPathSum(node.right))

            # Update the maximum path sum considering the current node as the root of the path
            maxSum = max(maxSum, node.data + leftMax + rightMax)

            # Return the maximum sum of the path including the current node and either left or right subtree
            return node.data + max(leftMax, rightMax)

        maxSum = float('-inf')  # Initialize max sum as the smallest possible value
        getMaxPathSum(root)
        return maxSum
