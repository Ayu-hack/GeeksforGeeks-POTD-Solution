class Solution {
  public:
    int maxDistance(vector<int> &arr) {
        // CodeGenius
        unordered_map<int,int>mp;
        int maxi=0;
        for(int i=0;i<arr.size();i++){
            if(mp.find(arr[i])!=mp.end()){//element hai
                maxi=max(maxi,i-mp[arr[i]]);
            }
            else {// element nahi hai
                   mp[arr[i]]=i;
            }
        }
        return maxi;
    }
};
