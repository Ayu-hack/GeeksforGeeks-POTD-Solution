class Solution {
    static Long reversedBits(Long x) {
        long result = 0;
        for(int i=0; i<32;i++){
            result <<= 1;
            if((x&1)==1){
                result |= 1;
            }
            x >>= 1;
        }
        return result;
      
    }
};
