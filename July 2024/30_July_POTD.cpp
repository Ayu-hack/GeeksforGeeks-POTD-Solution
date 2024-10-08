// User function template for C++

class Solution {
  public:
    int n;
    set<string>st;
    vector<vector<int>>vis;
    void rec(int i, int j, string cur, vector<vector<int>>&mat) {
        if(i < 0 or j < 0 or i >= n or j >= n or vis[i][j] or !mat[i][j]) return;
        if(i == n-1 and j == n-1) {
            st.insert(cur);
            // cout<<cur<<" ";
            return;
        }
        vis[i][j] = true;
        rec(i+1, j, cur + "D", mat);
        rec(i, j+1, cur + "R", mat);
        rec(i-1, j, cur + "U", mat);
        rec(i, j-1, cur + "L", mat);
        
        vis[i][j] = false;
        return;
    }
    vector<string> findPath(vector<vector<int>> &mat) {
        n = mat.size();
        if(!mat[n-1][n-1]) return {"-1"};
        vis.resize(n, vector<int>(n));
        rec(0, 0, "", mat);
        if(st.empty()) return {"-1"};
        vector<string>ans;
        for(auto i:st) ans.push_back(i);
        return ans;
    }
};