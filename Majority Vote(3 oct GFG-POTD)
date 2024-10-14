class Solution {
  public:
   vector<int> findMajority(vector<int>& nums) {
        vector<int>ans;
        unordered_map<int,int>mp;
        for(auto &it:nums){
            mp[it]++;
        }
        for(auto it:mp){
            if(it.second>(nums.size()/3)) ans.push_back(it.first);
        }
        sort(ans.begin(),ans.end());
        if(ans.size()==0) return {-1};
        return ans;
    }

};
