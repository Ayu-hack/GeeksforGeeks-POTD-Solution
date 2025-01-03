class Solution {
  public:
    long subarrayXor(vector<int> &arr, int k) {
        // code here
        int xor_=0,ans=0;
        unordered_map<int,int> mm;
        for(int x:arr){
            xor_^=x;
            if(xor_==k)ans++;
            ans+=mm[xor_^k];
            mm[xor_]++;
        }
        return ans;
    }

};
