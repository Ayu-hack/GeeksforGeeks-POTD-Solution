//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
    public:
    bool canPair(vector<int> nums, int k) {
        // Code here.
        int n=nums.size();
        if(n%2!=0) return 0;
        unordered_map<int, int>mpp;
        for(int i=0; i<n; i++){
            nums[i]%=k;
            if(nums[i]==0) continue;
            int conju=k-nums[i];
            if(mpp.find(conju)!=mpp.end()){
                mpp[conju]--;
                if(mpp[conju]==0) mpp.erase(conju);
            }else mpp[nums[i]]++;
        }
        return mpp.size()==0?1:0;
    }
};


//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, k;
        cin >> n >> k;
        vector<int> nums(n);
        for (int i = 0; i < nums.size(); i++) cin >> nums[i];
        Solution ob;
        bool ans = ob.canPair(nums, k);
        if (ans)
            cout << "True\n";
        else
            cout << "False\n";
    }
    return 0;
}
// } Driver Code Ends
