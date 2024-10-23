 public:
    // function should print the nodes at k distance from root
    vector<int> Kdistance(struct Node *root, int k)
    {
       queue<pair<Node*,int>> q;
        vector<int> ans;
        q.push({root,0});
        while(!q.empty()){
            int dist =q.front().second;
            Node* temp =q.front().first;
            
            if(!q.empty() and dist == k){
                ans.emplace_back(temp->data);
            }
            
            q.pop();
            if(temp->left != NULL){
                q.push({temp->left,dist +1});
            }
            if(temp->right != NULL){
                q.push({temp->right,dist +1});
            }
        }
        return ans;
    
    }
};
