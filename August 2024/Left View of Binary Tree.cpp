#Potd 23 aug 2024
#Left View of Binary Tree


cpp code

void solve(Node *root,vector<int> &ans,int level){
    if(!root) return;
    
    if(ans.size()==level)
    ans.push_back(root->data);
    solve(root->left,ans,level+1);
    solve(root->right,ans,level+1);
}

vector<int> leftView(Node *root)
{
   // Your code here
   vector<int> ans;
   solve(root,ans,0);
   return ans;
}
