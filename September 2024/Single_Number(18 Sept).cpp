class Solution {
  public:
    int getSingle(vector<int>& arr) {
        
        int maxx = INT_MIN;
        
        for(int i = 0; i < arr.size();  i++){
            
            maxx = max(maxx, arr[i]);
        }
        vector<int> hash(maxx+1, 0);
        
        for(int i = 0; i < arr.size(); i++){
            
            hash[arr[i]]++;
        }
        int ans = 0;
        
        for(int i = 0; i < hash.size(); i++){
            
            if(hash[i] % 2 != 0){
                
                ans = i;
                break;
            }
        }
        return ans;
        // code here
    }
};

