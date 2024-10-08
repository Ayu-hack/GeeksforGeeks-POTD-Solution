// User function Template for C++
class DSU {

public:
    vector<int> rank, parent, size;
    DSU(int n) {
        rank.resize(n + 1, 0);
        parent.resize(n + 1);
        size.resize(n + 1);
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int findUPar(int node) {
        if (node == parent[node])
            return node;
        return parent[node] = findUPar(parent[node]);
    }

    void unionByRank(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (rank[ulp_u] < rank[ulp_v]) {
            parent[ulp_u] = ulp_v;
        }
        else if (rank[ulp_v] < rank[ulp_u]) {
            parent[ulp_v] = ulp_u;
        }
        else {
            parent[ulp_v] = ulp_u;
            rank[ulp_u]++;
        }
    }

    void unionBySize(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (size[ulp_u] < size[ulp_v]) {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }
        else {
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
};
class Solution {
  public:
    
    int MaxConnection(vector<vector<int>>& grid) {
        int n = grid.size();
        DSU dsu(n*n);
        vector<pair<int, int>> dir = {{0,1}, {0,-1}, {-1,0}, {1,0}};
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(grid[i][j] == 0) continue;
                for(auto d:dir) {
                    int x = i + d.first, y = j + d.second;
                    if(x < 0 or x >= n or y < 0 or y >= n or grid[x][y] == 0) continue;
                    int cur_node = i * n + j;
                    int new_node = x * n + y;
                    dsu.unionBySize(cur_node, new_node);
                }
            }
        }
        int ans = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(grid[i][j] == 1) continue;
                set<int> cur;
                for(auto d:dir) {
                    int x = i + d.first, y = j + d.second;
                    if(x < 0 or x >= n or y < 0 or y >= n or grid[x][y] == 0) continue;
                    cur.insert(dsu.findUPar(x * n + y));
                }
                int temp = 0;
                for(auto st:cur) temp += dsu.size[st];
                ans = max(ans, temp + 1);
            }
        }
        for(int i=0; i<n*n; i++) {
            ans = max(ans, dsu.size[dsu.findUPar(i)]);
        }
        return ans;
    }
};