class Solution {
    public int kthSmallest(Node root, int k) {
        ArrayList<Integer> ls = new ArrayList<>();
        inorder(root,ls);
         if (k > 0 && k <= ls.size()) {
            return ls.get(k - 1); // kth element (1-based index)
        }
        
        return -1; // If k is out of bounds
    }
    public void inorder(Node root,ArrayList<Integer> ls){
        if(root == null){
            return;
        }
        inorder(root.left,ls);
        ls.add(root.data);
        inorder(root.right,ls);
    }
}
