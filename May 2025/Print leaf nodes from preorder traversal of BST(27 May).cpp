class Solution {
  public:
    vector<int> leafNodes(vector<int>& p) {
        stack<int> s;
        vector<int> r;
        for (int i = 0, j = 1; j < p.size(); i++, j++) {
            bool f = 0;
            if (p[i] > p[j]) s.push(p[i]);
            else while (!s.empty() && p[j] > s.top()) s.pop(), f = 1;
            if (f) r.push_back(p[i]);
        }
        r.push_back(p.back());
        return r;
    }
};
