class Solution {
  public:

    bool checkDuplicatesWithinK(vector<int>& arr, int k) {
        unordered_map<int,int> mp;
        int n=arr.size();
        if(n==1) return false;
        for(int i=0;i<=k;i++){
            mp[arr[i]]++;
            if(mp[arr[i]]>1) return true;
        }
        int last=0;
        for(int i=k+1;i<n;i++){
            mp[arr[last++]]--;
            mp[arr[i]]++;
            if(mp[arr[i]]>1) return true;
        }
        return false;
    }
};
