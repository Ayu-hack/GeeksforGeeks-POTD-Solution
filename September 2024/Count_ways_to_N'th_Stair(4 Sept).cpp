class Solution {
  public:
    int nthStair(int n) {
        
        if(n == 0){
            
            return 1;
        }
        
        double check;
        int cnt = 0;
        
        for(int i = n; i >= 1; i--){
            
            check = (double)n / i;
            
            if(check <= 2){
                
                cnt++;
            }
        }
        return cnt;
    
        //  Code here
    }
};
