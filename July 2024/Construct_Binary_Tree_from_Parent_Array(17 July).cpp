class Solution {
  public:
    // Function to construct binary tree from parent array.
    Node *createTree(vector<int> parent) {
        int n = parent.size();
        vector<Node*> nodes(n, nullptr);
        Node* root = nullptr;

        // Step 1: Create Node objects for each index
        for (int i = 0; i < n; i++) {
            nodes[i] = new Node(i);
        }

        // Step 2: Build the tree by linking parent and child nodes
        for (int i = 0; i < n; i++) {
            if (parent[i] == -1) {
                root = nodes[i]; // This is the root node
            } else {
                Node* parentNode = nodes[parent[i]];

                // If left child is null, assign as left child
                if (parentNode->left == nullptr) {
                    parentNode->left = nodes[i];
                } 
                // Otherwise, assign as right child
                else {
                    parentNode->right = nodes[i];
                }
            }
        }

        return root;
    }
};
