class Solution {
  public:
    TreeNode *rec(vector<int>&ar, int i) {
        if(i >= ar.size()) return NULL;
        TreeNode *root = new TreeNode(ar[i]);
        root->left = rec(ar, 2*i+1);
        root->right = rec(ar, 2*i+2);
        return root;
    }
    void convert(Node *head, TreeNode *&root) {
        Node *temp = head;
        vector<int>cur;
        while(temp != NULL) {
            cur.push_back(temp->data);
            temp = temp->next;
        }
        root = rec(cur, 0);
    }   
};