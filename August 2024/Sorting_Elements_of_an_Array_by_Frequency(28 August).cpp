class Solution {
  public:
  
  static bool cmp(pair<int, int> a, pair<int, int> b){

        if(a.second == b.second){

            return a.first < b.first;
        }
        else{

            return a.second > b.second;
        }
    }
    // Complete this function
    // Function to sort the array according to frequency of elements.
    vector<int> sortByFreq(vector<int>& arr) {
        
        map<int, int> mp;
        
        for(int i = 0; i < arr.size(); i++){
            
            mp[arr[i]]++;
        }
        
        vector<pair<int, int>> gg;
        
        
        for(auto it : mp){
            
            gg.push_back(make_pair(it.first, it.second));
        }
        
        sort(gg.begin(), gg.end(), cmp);
        
        vector<int> ans;
        
        for(int i = 0; i < gg.size(); i++){
            
            while(gg[i].second > 0){
                
                ans.push_back(gg[i].first);
                gg[i].second--;
            }
        }
        return ans;
        // Your code here
    }
};
