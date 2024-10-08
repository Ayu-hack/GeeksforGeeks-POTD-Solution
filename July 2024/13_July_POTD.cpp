class Solution {
  public:
    vector<int> shortestPath(int n, int m, vector<vector<int>>& edges) {
        vector<vector<pair<int, int>>> adj(n);
        for(auto i:edges) {
            i[0]--;
            i[1]--;
            adj[i[0]].push_back({i[1], i[2]});
            adj[i[1]].push_back({i[0], i[2]});
        }
        vector<int>dis(n, INT_MAX), par(n, -1);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>pq;
        pq.push({0, 0});
        dis[0] = 0;
        while(!pq.empty()) {
            int v = pq.top().second;
            int d_v = pq.top().first;
            pq.pop();
            if(d_v != dis[v]) continue;
            for(auto u:adj[v]) {
                int to = u.first;
                int len = u.second;
                if(dis[to] > len + dis[v]) {
                    dis[to] = dis[v] + len;
                    pq.push({dis[to], to});
                    par[to] = v;
                }
            }
        }
        if(dis[n-1] == INT_MAX) return {-1};
        vector<int> ans;
        ans.push_back(dis[n-1]);
        stack<int>cur;
        int c = n-1;
        while(c != -1) {
            cur.push(c);
            c = par[c];
        }
        while(!cur.empty()) ans.push_back(cur.top() + 1), cur.pop();
        return ans;
        
    }
};