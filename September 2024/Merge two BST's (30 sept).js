// JAVA CODE

class Solution {
    // Function to return a list of integers denoting the node
    // values of both the BST in a sorted order.
    void help(Node root,List<Integer> temp){
        if(root==null)return;
        help(root.left,temp);
        temp.add(root.data);
        help(root.right,temp);
    }
    // Function to return a list of integers denoting the node
    // values of both the BST in a sorted order.
    public List<Integer> merge(Node root1, Node root2) {
        // Write your code here
        List<Integer> first = new ArrayList<>();
        List<Integer> second = new ArrayList<>();
        List<Integer> ans = new ArrayList<>();
        help(root1,first);
        help(root2,second);
        int i=0,j=0;
        while(i<first.size() && j<second.size()){
            if(first.get(i)<=second.get(j))ans.add(first.get(i++));
            else ans.add(second.get(j++));
        }
        while(i<first.size())ans.add(first.get(i++));
        while(j<second.size())ans.add(second.get(j++));
        return ans;
    }
}
