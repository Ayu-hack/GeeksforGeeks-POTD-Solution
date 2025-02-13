class Solution {
    boolean findTarget(Node root, int target) {
        // Write your code here
        if(root == null){
            return false;
        }
        return solve(root, root, target);
    }
    boolean solve(Node root, Node curr, int target){
        if(curr == null){
            return false;
        }
        if(findNode(root, target-curr.data, curr)){
            return true;
        }
        return solve(root, curr.left, target) || solve(root, curr.right, target);
    }
    boolean findNode(Node root, int target, Node curr){
        if(root==null){
            return false;
        }
        if(root.data == target && root != curr) {
            return true;
        }
        if(root.data > target){
            return findNode(root.left, target, curr);
        }
        return findNode(root.right, target, curr);
    }
}
