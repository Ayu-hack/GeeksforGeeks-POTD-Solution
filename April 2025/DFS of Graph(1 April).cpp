class Solution {
    public:
      void dfs(int i, vector<vector<int>> &adj, vector<int> &ans, unordered_map<int, bool> &visited){
          ans.push_back(i);
          visited[i] = true;
          for(auto z : adj[i]){
              if(!visited[z]){
                  dfs(z, adj, ans, visited);
              }
          }
          return;
      }
      vector<int> dfs(vector<vector<int>>& adj) {
          vector<int> ans;
          unordered_map<int, bool> visited;
          dfs(0, adj, ans, visited);
          return ans;
      }
  };
