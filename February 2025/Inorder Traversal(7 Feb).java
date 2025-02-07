class Solution {
    // Function to return a list containing the inorder traversal of the tree.
    ArrayList<Integer> inOrder(Node root) {
        // Code
        ArrayList<Integer> ans = new ArrayList();
        Stack<Node> st = new Stack();
        while(root!=null){
            st.push(root);
            root=root.left;
        }
        while(!st.isEmpty()){
            Node tmp = st.pop();
            ans.add(tmp.data);
            if(tmp.right!=null){
                tmp = tmp.right;
                while(tmp!=null){
                    st.push(tmp);
                    tmp = tmp.left;
                }
            }
        }
        return ans;
    }
}
