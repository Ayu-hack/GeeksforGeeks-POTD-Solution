//JAVA CODE

class Solution {
    public long findSmallest(int[] arr) {
        // Your code goes here
        long ans = 1;
        for(int x:arr){
            if(x>ans)return ans;
            ans+=x;
        }
        return ans;
    }
}
