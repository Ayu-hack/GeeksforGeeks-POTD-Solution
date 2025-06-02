class Solution {
  public:
    int uniquePaths(vector<vector<int>> &grid) {
        int r = grid.size(), c = grid[0].size();
        vector<int> dp(c);
        dp[0] = grid[0][0] == 0;
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)Add commentMore actions
                if (grid[i][j]) dp[j] = 0;
                else if (j) dp[j] += dp[j - 1];
        return dp[c - 1];
    }
};
