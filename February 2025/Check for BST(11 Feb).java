class Solution {
    void inorder(Node root, List<Integer> h) {
        if (root == null) {
            return;
        }
        // LNR
        inorder(root.left, h);
        h.add(root.data);
        inorder(root.right, h);
    }

    boolean isBST(Node root) {
        List<Integer> h = new ArrayList<>();
        inorder(root, h);
        for (int i = 1; i < h.size(); i++) {
            if (h.get(i) <= h.get(i - 1)) {
                return false;
            }
        }
        return true;
    }
}
