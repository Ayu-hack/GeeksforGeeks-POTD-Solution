class Solution {
    public int getSingle(int[] arr) {
        // code here
        int res = 0;
        for(int i = 0; i < 32; ++i){
            int cnt = 0;
            int x = 1 << i;
            for(int j = 0 ; j < arr.length; ++j){
                if((arr[j] & x) != 0){
                    cnt++;
                }
            }
            
            if(cnt % 3 != 0){
                res |= x;
            }
        }
        
        return res;
    }
}
