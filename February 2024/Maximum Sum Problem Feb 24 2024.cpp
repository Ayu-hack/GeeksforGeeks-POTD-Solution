class Solution {
public:
    int maxSum(int n) {
        vector<int> dp(n+1, 0);
        for(int i = 1; i <= n; ++i) {
            dp[i] = dp[i/2] + dp[i/3] + dp[i/4];
            dp[i] = max(dp[i], i);
        }
        return dp[n];
    }
};
