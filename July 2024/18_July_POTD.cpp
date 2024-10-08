class Solution {
  public:
    int find(vector<int>& arr, vector<vector<int>>& dp, int i, int n, bool isIncreasing) {
        if (i >= n) return 0;
        
        if (dp[i][isIncreasing] != -1) {
            return dp[i][isIncreasing];
        }
        
        int nottake = find(arr, dp, i + 1, n, isIncreasing);
        int take = -1e9;
        
        if (isIncreasing) {
           
            if (i == 0 || arr[i] > arr[i - 1]) {
                take = 1 + find(arr, dp, i + 1, n, !isIncreasing);
            }
        } else {
            
            if (i == 0 || arr[i] < arr[i - 1]) {
                take = 1 + find(arr, dp, i + 1, n, !isIncreasing);
            }
        }
        
        return dp[i][isIncreasing] = max(take, nottake);
    }
    int alternatingMaxLength(vector<int>& arr) {
        // Code here
          int n = arr.size();
        vector<vector<int>> dp(n, vector<int>(2, -1));
        
        int inc = find(arr, dp, 0, n, true);
        int dec = find(arr, dp, 0, n, false);
        
        return max(inc, dec);
    }
};