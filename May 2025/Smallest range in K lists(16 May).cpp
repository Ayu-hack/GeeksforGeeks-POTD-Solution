class Solution {
public:
    struct Node {
        int v, r, c;
        bool operator>(const Node& o) const { return v > o.v; }
    };
    vector<int> findSmallestRange(vector<vector<int>>& a) {
        int n = a.size(), m = a[0].size(), hi = INT_MIN, lo = 0, r = 1e9;
        priority_queue<Node, vector<Node>, greater<Node>> q;
        for (int i = 0; i < n; i++) q.push({a[i][0], i, 0}), hi = max(hi, a[i][0]);
        while (1) {
            auto x = q.top(); q.pop();
            if (hi - x.v < r - lo) lo = x.v, r = hi;
            if (x.c + 1 == m) break;
            int y = a[x.r][x.c + 1];
            q.push({y, x.r, x.c + 1});
            hi = max(hi, y);
        }
        return {lo, r};
    }
};
