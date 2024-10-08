/* node structure  used in the program

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
}; */

class Solution {
  public:
    // Function to construct binary tree from parent array.
    unordered_map<int, vector<int>>mp;
    void rec(Node *root) {
        if(root == NULL) return;
        if(mp.find(root->data) != mp.end()) {
            if(mp[root->data].size() == 2) {
                root->left = new Node(mp[root->data][0]);
                rec(root->left);
                root->right = new Node(mp[root->data][1]);
                rec(root->right);
            }
            else {
                root->left = new Node(mp[root->data][0]);
                rec(root->left);
            }
        }
    }
    Node *createTree(vector<int> par) {
              // Your code here
        Node *root;
        for(int i=0; i<par.size(); i++) {
            if(par[i] == -1) root = new Node(i);
            else mp[par[i]].push_back(i);
        }
        rec(root);
        return root;
    }
};