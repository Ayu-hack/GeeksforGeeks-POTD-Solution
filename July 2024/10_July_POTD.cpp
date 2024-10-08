// User function Template for C++

class Solution {
  public:
    int rec(int i, int j, int n, int m, vector<vector<int>>&dp, vector<vector<int>>&mat) {
        if(i >= n or j >= m) return 0;
        if(dp[i][j] != -1) return dp[i][j];
        
        int down = rec(i+1, j, n, m, dp, mat);
        int up = rec(i, j+1, n, m, dp, mat);
        int d = rec(i+1, j+1, n, m, dp, mat);
        
        dp[i][j] = 0;
        if(mat[i][j] == 1) {
            dp[i][j] = 1 + min(up, min(down, d));
        }
        return dp[i][j];
    }
    int maxSquare(int n, int m, vector<vector<int>> mat) {
        // code here
        vector<vector<int>> dp(n, vector<int>(m, -1));
        rec(0,0,n,m,dp,mat);
        int mx = -1;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) mx = max(mx, dp[i][j]);
        }
        return mx;
        
    }
};