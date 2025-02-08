class Solution {
    ArrayList<Integer> boundaryTraversal(Node node) {
        // code here
        ArrayList<Integer> ans = new ArrayList();
        if(node.left!=null || node.right!=null){
            ans.add(node.data);
        }
        leftNodes(node.left, ans);
        addLeaves(node, ans);
        rightRevNodes(node.right, ans);
        return ans;
    }
    void leftNodes(Node node, ArrayList<Integer> ans){
        if(node == null)
            return;
        if(node.left!=null){
            ans.add(node.data);
            leftNodes(node.left, ans);
        } else if(node.right!=null){
             ans.add(node.data);
            leftNodes(node.right, ans);
        }
    }
    void addLeaves(Node node, ArrayList<Integer> ans){
        if(node == null)
            return;
        addLeaves(node.left, ans);
        if(node.left==null && node.right == null){
             ans.add(node.data);
        }
         addLeaves(node.right, ans);
    }
    void rightRevNodes(Node node, ArrayList<Integer> ans){
        if(node == null)
            return;
        if(node.right!=null){
            
            rightRevNodes(node.right, ans);
            ans.add(node.data);
        } else if(node.left!=null){
            rightRevNodes(node.left, ans);
            ans.add(node.data);
        }
    }
}
