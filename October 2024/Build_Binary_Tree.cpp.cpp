#include <iostream>
using namespace std;

class node
{
public:
    int data;
    node *left;
    node *right;

    node(int d)
    {
        this->data = d;
        this->left = NULL;
        this->right = NULL;
    }
};

//data enter karna ka one of the tarika in binary tree

node *buildTree(node *root)
{
    cout << "Enter the data" << endl;
    int data;
    cin >> data;
    root=new node(data);
    if (data == -1)
    {
        return NULL;
    }

    cout << "Enter the data for left side of " << data << endl;
    root->left = buildTree(root->left);

    cout << "Enter the data for right side of " << data << endl;
    root->right = buildTree(root->right);

    return root;
}
int main()
{
    node *root = NULL;

    root = buildTree(root);
}