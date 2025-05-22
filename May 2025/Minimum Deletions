
class Solution {
  public:
    int minDeletions(string &s) {
        int n = s.size();
        vector<int> dp(n), prev(n);
        for (int i = n - 1; i >= 0; --i) {
            dp[i] = 1;
            for (int j = i + 1; j < n; ++j)
                dp[j] = s[i] == s[j] ? prev[j - 1] + 2 : max(prev[j], dp[j - 1]);
            prev = dp;
        }
        return n - dp[n - 1];
    }
};
