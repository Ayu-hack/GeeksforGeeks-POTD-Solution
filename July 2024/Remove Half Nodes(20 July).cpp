// Base case: if the current node is null, return null
    if (!root) return nullptr;

    // Recursively call for left and right children
    root->left = removeHalfNodes(root->left);
    root->right = removeHalfNodes(root->right);

    // If the current node is a half node, return the non-null child
    if (!root->left && root->right) {
        return root->right; // Only right child
    }
    if (!root->right && root->left) {
        return root->left; // Only left child
    }

    // If it's not a half node, return the current node
    return root;