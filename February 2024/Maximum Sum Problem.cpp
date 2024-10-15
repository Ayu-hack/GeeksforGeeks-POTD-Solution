//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    public:
      unordered_map<int, int> memo;

    int maxSum(int n) {
     
        if (n == 0) return 0;
        if (memo.find(n) != memo.end()) return memo[n];
        int sum = maxSum(n / 2) + maxSum(n / 3) + maxSum(n / 4);
        memo[n] = max(n, sum);
        return memo[n];
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        Solution ob;
        cout<<ob.maxSum(n)<<"\n";
    }
    return 0;
}
// } Driver Code Ends
