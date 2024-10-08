/*Complete the function below
Node is as follows:
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/

// Return the root of the modified tree after removing all the half nodes.
class Solution {
  public:
    Node *RemoveHalfNodes(Node *root) {
        // code here
        if(root == NULL or (root->left == NULL and root->right == NULL)) return root;
        if(root->left == NULL) return RemoveHalfNodes(root->right);
        if(root->right == NULL) return RemoveHalfNodes(root->left);
        
        root->left = RemoveHalfNodes(root->left);
        root->right = RemoveHalfNodes(root->right);
        return root;
        
    }
};