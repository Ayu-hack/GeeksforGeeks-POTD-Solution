class Solution {
    static int pos;
    public static Node buildTree(int inorder[], int preorder[]) {
        // code here
        pos = 0;
        return solve(inorder, preorder, 0, inorder.length-1);
    }
    static Node solve(int inorder[], int preorder[], int str, int end){
        if(str>inorder.length || str> end){
            return null;
        }
        Node root = new Node(preorder[pos]);
        int div = 0;
        for(int i=str;i<=end;i++){
            if(preorder[pos] == inorder[i]){
                div = i;
                break;
            }
        }
        pos++;
        root.left = solve(inorder, preorder, str, div-1);
        root.right = solve(inorder, preorder, div+1, end);
        return root;
    }
}
