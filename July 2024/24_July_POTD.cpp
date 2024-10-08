class Solution {
  public:
    // Function to check whether a Binary Tree is BST or not.
    vector<int>path;
    void rec(Node *r) {
        if(r == NULL) return;
        rec(r->left);
        path.push_back(r->data);
        rec(r->right);
    }
    bool isBST(Node* root) {
        // Your code here
        rec(root);
        // bool ans = true;
        for(int i=1; i<path.size(); i++) {
            if(path[i-1] >= path[i]) return false;
        }
        return true;
    }
};