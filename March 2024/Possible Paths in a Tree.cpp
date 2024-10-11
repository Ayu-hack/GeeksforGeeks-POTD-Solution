//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++


//User function template for C++
void dfs(int u,vector<bool> &vis, vector<pair<int,int>> adj[],vector<int> &vec,int q){
    vis[u]=true;
    vec.push_back(u);
    
    for(auto v:adj[u]){
    if(vis[v.first]==false && v.second<=q)
    dfs(v.first,vis,adj,vec,q);
        
    }
    return;
}
class Solution{
	public:
	vector<int> maximumWeight(int n, vector<vector<int>> edges, int q, vector<int> &queries)
	{
	    // code here
	    vector<pair<int,int>> adj[n];
	    for(int i=0;i<edges.size();i++)
	    {
	        adj[edges[i][0]-1].push_back({edges[i][1]-1,edges[i][2]});
	        adj[edges[i][1]-1].push_back({edges[i][0]-1,edges[i][2]});
	        
	    }
	    vector<int> t;
	    vector<int> vec;
	    
	    for(int j=0;j<q;j++){
	        vector<bool> vis(n,false);
	        vec.clear();
	    for(int i=0;i<n;i++)
	    {
	        if(vis[i]==false)
	        {
	            dfs(i,vis,adj,vec,queries[j]);
	            vec.push_back(-1);
	        }
	    }
	    int pre=0,ans=0;
	    for(int k=0;k<vec.size();k++){
	        if(vec[k]==-1){
	            ans+=((k-pre)*(k-pre-1))/2;
	            pre=k+1;
	        }
	    }
	    
	    ans+=((vec.size()-pre)*(vec.size()-pre-1))/2;
	    t.push_back(ans);
	    
	    }
	    return t;
	}
};


//{ Driver Code Starts.

int main() 
{
   	int t;
    cin >> t;
    while (t--)
    {
    	int n;
        cin >> n;
        
        vector<vector<int>> edges(n-1, vector<int> (3, 0));

        for(int i = 0; i < n-1; i++)
        {
        	for(int j = 0; j < 3; j++)
        	{
        		cin >> edges[i][j];
        	}
        }

        int q;
        cin >> q;
        vector<int> queries(q);
        for(int i = 0; i < q; i++)
        	cin >> queries[i];

    	Solution obj;
    	vector<int> ans = obj.maximumWeight(n, edges, q, queries);

    	for(auto i:ans)
    		cout << i << " ";
    	cout << "\n"; 
    }
    return 0;
}

// } Driver Code Ends
