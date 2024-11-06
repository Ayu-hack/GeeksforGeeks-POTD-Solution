class Solution {
     public static int help(Node root,int num){
        if(root==null)return 0;
        num = num*10+root.data;
        if(root.left==null && root.right==null)return num;
        return help(root.left,num)+help(root.right,num);
    }
    public static int treePathsSum(Node root) {
        // add code here.
        return help(root,0);
    }
}
