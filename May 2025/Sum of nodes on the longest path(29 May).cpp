class Solution {
  public:
    void sumOfRootToLeaf(Node* r, int s, int l, int& ml, int& ms) {
        if (!r) {
            if (l > ml) ml = l, ms = s;
            else if (l == ml && s > ms) ms = s;
            return;
        }
        sumOfRootToLeaf(r->left, s + r->data, l + 1, ml, ms);
        sumOfRootToLeaf(r->right, s + r->data, l + 1, ml, ms);
    }
    int sumOfLongRootToLeafPath(Node* root) {
        int ms = INT_MIN, ml = 0;
        sumOfRootToLeaf(root, 0, 0, ml, ms);
        return ms;
    }
};
