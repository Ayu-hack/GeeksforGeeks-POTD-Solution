class Solution {
    public boolean isCyclic(int V, int[][] edges) {
        // code here
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }
        
        for (int[] edge : edges){
            adj.get(edge[0]).add(edge[1]);
        }
        
        int n = adj.size();
        
        boolean[] vis = new boolean[n];
        boolean[] path = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (!vis[i] && dfs(i, adj, vis, path)) {
                return true;
            }
        }
        
        return false;
    }
    
    private boolean dfs(int i, ArrayList<ArrayList<Integer>> adj, boolean[] vis, boolean[] path) {
        vis[i] = true;
        path[i] = true;
    
        
        for (int node : adj.get(i)) {
            if (path[node]) {
                return true;
            }
            
            if (!vis[node]) {
                if (dfs(node, adj, vis, path)) {
                    return true;
                }
            }
        }
        
        path[i] = false;
        return false;
    }
}
