//Back-end complete function Template for C++
class Solution {
  public:
    // Function to find the vertical width of a Binary Tree.
    int mn = 0, mx = 0;
    void rec(Node *root, int x) {
        if(root == NULL) return;
        mn = min(mn, x);
        mx = max(mx, x);
        rec(root->left, x - 1);
        rec(root->right, x + 1);
    }
    int verticalWidth(Node* root) {
        // code here
        if(root == NULL) return 0;
        rec(root, 0);
        return mx - mn + 1;
    }
};