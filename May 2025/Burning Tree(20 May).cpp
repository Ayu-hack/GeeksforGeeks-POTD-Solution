class Solution {
  public:
    Node* key = nullptr;
    void inorder(Node* root, int& target, unordered_map<Node*, Node*>& mp) {
        if (!root) return;
        if (root->left) {
            mp[root->left] = root;
            inorder(root->left, target, mp);
        }
        if (root->data == target) key = root;
        if (root->right) {
            mp[root->right] = root;
            inorder(root->right, target, mp);
        }
    }
    int minTime(Node* root, int target) {
        // code here
        unordered_map<Node*, Node*> mp;
        unordered_map<Node*, bool> vis;
        inorder(root, target, mp);
        int t = -1;
        queue<Node*> q;
        q.push(key);
        vis[key] = true;
        while (!q.empty()) {
            int size = q.size();
            while (size--) {
                Node* node = q.front();
                q.pop();
                if (node->left && !vis[node->left]) {
                    vis[node->left] = true;
                    q.push(node->left);
                }
                if (node->right && !vis[node->right]) {
                    vis[node->right] = true;
                    q.push(node->right);
                }
                if (mp[node] && !vis[mp[node]]) {
                    vis[mp[node]] = true;
                    q.push(mp[node]);
                }
            } t++;
        } return t;
    }
};
