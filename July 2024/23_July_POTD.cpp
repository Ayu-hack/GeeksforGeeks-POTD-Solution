/*
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
class Solution {
  public:
    // Function to return a list of integers denoting the node
    // values of both the BST in a sorted order.
    multiset<int>st;
    void f(Node *r) {
        if(r == NULL) return;
        f(r->left);
        st.insert(r->data);
        f(r->right);
    }
    vector<int> merge(Node *root1, Node *root2) {
        // Your code here
        f(root1);
        f(root2);
        return vector<int>(st.begin(), st.end());
    }
};