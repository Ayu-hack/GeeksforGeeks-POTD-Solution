class Solution {
  public:
    int pairWithMaxSum(vector<int>& arr) {
        
        int ans = INT_MIN;
        int n = arr.size();
        
        if(n < 2){
            return -1;
        }
        
        for(int i = 0; i < n-1; i++){
            
            int sum = arr[i] + arr[i+1];
            
            ans = max(ans, sum);
            
        }
        return ans;
        // code here
    }
};

