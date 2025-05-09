class Solution {
  public:
    string ans;
    void solve(string &s, int k, int idx) {
        if (k == 0) return;
        char mx = *max_element(s.begin() + idx, s.end());
        if (mx != s[idx]) k--;
        for (int i = s.size() - 1; i >= idx; i--) {
            if (s[i] == mx) {
                swap(s[i], s[idx]);
                if (s > ans) ans = s;
                solve(s, k, idx + 1);
                swap(s[i], s[idx]);
            }
        }
    }
    string findMaximumNum(string& s, int k) {
        ans = s;
        solve(s, k, 0);
        return ans;
    }
};
