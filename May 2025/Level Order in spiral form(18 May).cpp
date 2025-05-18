class Solution {
public:
    vector<int> findSpiral(Node* root) {
        vector<int> result; // To store the final spiral order traversal

        if (root == nullptr) {
            return result; // Edge case: empty tree
        }

        queue<Node*> que; // Queue for level order traversal
        que.push(root);

        bool direction = false; // false => right to left, true => left to right

        while (!que.empty()) {
            int         n = que.size(); // Number of nodes at current level
            vector<int> row(n);         // Temporary vector to store current level's values

            for (int i = 0; i < n; i++) {
                Node* node = que.front();
                que.pop();

                // Determine index based on current direction
                int idx = direction ? i : (n - 1 - i);
                row[idx] = node->data; // Place node's value at calculated index

                if (node->left) {
                    que.push(node->left); // Add left child to queue
                }

                if (node->right) {
                    que.push(node->right); // Add right child to queue
                }
            }

            // Append current level's values to result
            for (int val : row) {
                result.push_back(val);
            }

            direction = !direction; // Toggle direction for next level
        }
        return result;
    }
};
