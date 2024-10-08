/*
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val)
        : data(val)
        , left(nullptr)
        , right(nullptr) {}
};
*/

class Solution {
  public:
    int n;
    Node *rec(int l, int r, vector<int>&ar) {
        if(l >= r) return NULL;
        int mid = l + (r - l)/2;
        Node *cur = new Node(ar[mid]);
        cur->left = rec(l, mid - 1, ar);
        cur->right = rec(mid + 1, r, ar);
        return cur;
    }
    Node* sortedArrayToBST(vector<int>& nums) {
        // Code here
        n = nums.size();
        return rec(0, n-1, nums);
    }
};