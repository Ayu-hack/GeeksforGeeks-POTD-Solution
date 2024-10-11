class Solution {
  public:
    vector<int> rearrange(const vector<int>& arr) {
        
        map<int, int> mp;
        
        vector<int> ans;
        
        
        
        for(int i = 0; i < arr.size(); i++){
            
            mp[arr[i]]++;
        }
        
        for(int i = 0; i < arr.size(); i++){
            
            if(mp.find(i) == mp.end()){
                
                ans.push_back(-1);
            }
            else{
                
                ans.push_back(i);
            }
        }
        return ans;
        // Code here
    }
};

