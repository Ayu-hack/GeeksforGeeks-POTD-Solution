/*
struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
    struct Node *next;

    Node(int x)
    {
        data = x;
        left = NULL;
        right = NULL;
        next = NULL;
    }
};
*/
class Solution {
  public:
    Node *cur = NULL;
    void populateNext(Node *root) {
        // code here
        if(root == NULL) return;
        populateNext(root->right);
        root->next = cur;
        cur = root;
        populateNext(root->left);
    }
};