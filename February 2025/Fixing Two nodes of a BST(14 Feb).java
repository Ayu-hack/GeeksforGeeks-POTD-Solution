class Solution {
    Node first, middle, last, prev;
    private void inorder(Node root) {
        if (root == null) return;
        // Left subtree
        inorder(root.left);
        // Detect misplaced nodes
        if (prev != null && prev.data > root.data) {
            if (first == null) {
                first = prev;
                middle = root; // First violation
            } else {
                last = root; // Second violation
            }
        }
        prev = root; // Update prev node
        // Right subtree
        inorder(root.right);
    }
    void correctBST(Node root) {
        // code here.
         first = middle = last = null;
        inorder(root);
        // If two nodes are not adjacent
        if (first != null && last != null) {
            int temp = first.data;
            first.data = last.data;
            last.data = temp;
        }
        // If two nodes are adjacent in in-order traversal
        else if (first != null && middle != null) {
            int temp = first.data;
            first.data = middle.data;
            middle.data = temp;
        }
    }
}
