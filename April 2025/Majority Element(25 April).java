class Solution {
static int majorityElement(int arr[]) {
        // code here
        int candidate = 0;
        for(int i = 0; i < 32; ++i){
            int x = 1 << i;
            int count = 0;
            for(int j = 0 ;j < arr.length; ++j){
                if((arr[j] & x) != 0){
                    ++count;
                }
            }
            
            if(count > arr.length / 2){
                candidate |= x;
            }
        }
        
        int count = 0;
        for(int num : arr){
            if(candidate== num){
                ++count;
            }
        }
        
        return count > arr.length / 2 ? candidate : -1;
    }
}
