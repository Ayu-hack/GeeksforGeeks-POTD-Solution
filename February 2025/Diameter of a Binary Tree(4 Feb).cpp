class Solution {
  public:
    int go(Node* n, int* dia) {
        if (!n)
            return 0;
        int l = go(n->left, dia);
        int r = go(n->right, dia);
        if (l + r + 1 > *dia)
            *dia = l + r + 1;
        return 1 + max(l, r);
    }
    int diameter(Node* root) {
        int dia = 0;
        go(root, &dia);
        return dia - 1;
    }
};
