#GFG POTD 22 JAN 2024
# Paths from root with a specified sum
# cpp Program 

class Solution
{
    public:
    vector<vector<int>> printPaths(Node *root, int sum)
    {
        //code here
        vector<vector<int>> ans;
        vector<int> p;
        
        
        function(root, 0, sum, ans, p);
        
        return ans;
    }
    
    void function(Node * root, int curr, int sum, vector<vector<int>> & ans, vector<int> p)
    {
        if(root==NULL){
            return;
        }
        
        curr=curr+root->key;
        p.push_back(root->key);
        if(curr==sum){
            ans.push_back(p);
        }
        
        function(root->left, curr, sum, ans, p);
        function(root->right, curr, sum, ans, p);
        
    }
};
