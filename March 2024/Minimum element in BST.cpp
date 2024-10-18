#include <iostream>

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Function to find the minimum element in the given BST.
int minValue(Node* root) {
    if (root == nullptr) return -1; // Handle empty tree

    while (root->left != nullptr) {
        root = root->left; // Traverse to the leftmost node
    }
    
    return root->data; // Return the minimum value
}

// Function to insert a new value into the BST
Node* insert(Node* root, int val) {
    if (root == nullptr) {
        return new Node(val); // Create a new node if the tree is empty
    }
    if (val < root->data) {
        root->left = insert(root->left, val); // Insert in the left subtree
    } else {
        root->right = insert(root->right, val); // Insert in the right subtree
    }
    return root; // Return the unchanged root pointer
}

int main() {
    Node* root = nullptr; // Initialize an empty BST

    // Insert values into the BST
    root = insert(root, 15);
    insert(root, 10);
    insert(root, 20);
    insert(root, 8);
    insert(root, 12);
    insert(root, 17);
    insert(root, 25);

    // Find and print the minimum value in the BST
    int minVal = minValue(root);
    std::cout << "The minimum value in the BST is: " << minVal << std::endl;

    return 0;
}

//saurabh-23232
