// User function template for C++

/*
Structure of a node is as following
struct Node {
     int data;
     struct Node* left;
     struct Node* right;
};
*/

class Solution {
  public:
    // Function should return all the ancestor of the target node
    bool rec(Node *root, int k, vector<int>&ans) {
        if(root == NULL) return false;
        if(root->data == k) return true;
        bool chk = rec(root->left, k, ans) or rec(root->right, k, ans);
        if(chk) ans.push_back(root->data);
        else return false;
    }
    vector<int> Ancestors(struct Node *root, int target) {
        vector<int> ans;
        bool chk = rec(root, target, ans);
        return ans;
    }
};