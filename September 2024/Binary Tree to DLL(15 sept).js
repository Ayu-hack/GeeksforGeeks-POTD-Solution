
//JAVA CODE

class Solution
{
    //Function to convert binary tree to doubly linked list and return it.
    Node head = null, lastNode = null;
    void help(Node root){
        if(root==null)return;
        help(root.left);
        if(head==null)head=root;
        if(lastNode!=null)lastNode.right=root;
        root.left=lastNode;
        lastNode=root;
        help(root.right);
    }
    //Function to convert binary tree to doubly linked list and return it.
    Node bToDLL(Node root)
    {
	  //  Your code here	
	    help(root);
	    return head;
    }
}
