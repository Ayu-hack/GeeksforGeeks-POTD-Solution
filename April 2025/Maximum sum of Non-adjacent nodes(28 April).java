class Solution {
    public int[] dfs(Node root) {
        if(root == null) return new int[]{0,0};
        int left[] = dfs(root.left) , right[] = dfs(root.right);
        
        int include = root.data + left[1] + right[1];
        int exclude = Math.max(left[0],left[1]) + Math.max(right[0],right[1]);
        
        return new int[]{include,exclude};
    }
    // Function to return the maximum sum of non-adjacent nodes.
    public int getMaxSum(Node root) {
        // code here
        int[] both = dfs(root);
        return Math.max(both[0],both[1]);
    }
}
