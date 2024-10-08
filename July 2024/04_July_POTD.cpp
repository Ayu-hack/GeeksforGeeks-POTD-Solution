class Solution {
  public:
    vector<Node*>ans;
    unordered_map<string, int> mp;
    string rec(Node *root) {
        if(root == NULL) return "";
        string l = rec(root->left);
        string r = rec(root->right);
        string cur = to_string(root->data) + l + r;
        if(mp[cur] == 1) {
            ans.push_back(root);
        }
        mp[cur]++;
        return cur;
        
    }
    vector<Node*> printAllDups(Node* root) {
       string r = rec(root);
       return ans;
    }
};