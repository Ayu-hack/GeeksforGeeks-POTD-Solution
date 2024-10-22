class Solution {
  public:
    int countgroup(vector<int>& arr) {
        //CodeGenius
        int mod=1e9+7;
        int xr=0;
        int  n= arr.size();
        for(int i=0;i<arr.size();i++){
            xr^=arr[i];
        }
        if(xr!=0) return 0;
        int ans=1;
        for(int i=0;i<n-1;i++){
            ans=(ans*2)%mod;
        }
        return ans-1;
    }
};
