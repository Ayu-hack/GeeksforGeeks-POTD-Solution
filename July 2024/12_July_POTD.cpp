/* A binary tree node
struct Node
{
    int data;
    Node* left, * right;
}; */

/*you are required to
complete this function */
class Solution {
  public:
    bool hasPathSum(Node *root, int target) {
        if(root == NULL) return false;
        if(root->left == NULL and root->right == NULL) return root->data == target;
        bool left, right;
        // cout<<target<<" ";
        left = hasPathSum(root->left, target - (root->data));
        right = hasPathSum(root->right, target - (root->data));
        return left or right;
    }
};