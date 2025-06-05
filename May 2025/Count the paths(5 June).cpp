class Solution {
  public:
    int dfs(int u, int dest, vector<vector<int>> &adj, vector<int> &memo) 
    {
        if (u == dest) return 1;
    
        if (memo[u] != -1) return memo[u];
    
        int count = 0;
        for (int v : adj[u]) 
        {
            count += dfs(v, dest, adj, memo);
        }
    
        return memo[u] = count;
    }

int countPaths( vector<vector<int>> &edges, int V, int src, int dest) {
        vector<vector<int>> adj(V);
        vector<int> memo(V, -1);
    
        for (auto e: edges) {
            adj[e[0]].push_back(e[1]);
        }
    
        return dfs(src, dest, adj, memo);
    }
};
