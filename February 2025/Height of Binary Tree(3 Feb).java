class Solution {
    // Function to find the height of a binary tree.
    int height(Node node) {
        // code here
        if(node == null){
            return -1;
        }
        return Math.max(height(node.left), height(node.right))+1;
    }
}
