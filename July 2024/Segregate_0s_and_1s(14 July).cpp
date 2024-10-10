class Solution {
  public:
    void segregate0and1(vector<int> &arr) {
        
        map<int, int> mp;
        
        for(int i = 0; i < arr.size(); i++){
            
            mp[arr[i]]++;
        }
        
        arr.clear();
        
        while(mp[0] != 0){
            
            arr.push_back(0);
            mp[0]--;
        }
        while(mp[1] != 0){
            
            arr.push_back(1);
            mp[1]--;
        }
        // code here
    }
};
