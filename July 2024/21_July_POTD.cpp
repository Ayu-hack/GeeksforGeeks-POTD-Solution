// User function Template for C++
class Solution {
  public:
    
    long long int findMaxProduct(vector<int>& arr) {
        // Write your code here
        if(arr.size() == 1) return arr[0];
        long long int mod = 1e9+7, ans = 1, neg = -1e18, zc = 0, nc = 0;
        for(auto i:arr) {
            if(i == 0) {
                zc++;
                continue;
            }
            if(i < 0) {
                nc++;
                neg = max(neg, 1LL * i);
            }
            ans = (ans * 1LL * i)%mod;
        }
        if(zc == arr.size()) return 0;
        if(!(nc&1)) return ans;
        if(nc == 1 and zc > 0 and nc + zc == arr.size()) return 0;
        else return ans/neg; 
    }
};