class Solution {
   public int maxLen(int[] arr) {
        // Your code here
        HashMap<Integer,Integer> prefixSum = new HashMap<>();
        int n=arr.length,sum=0,ans=0;
        for(int i=0;i<n;i++){
            sum+=arr[i]==1?1:-1;
            if(sum==0){
                ans=i+1;
            }
            if(prefixSum.get(sum)!=null){
                ans=Math.max(ans,i-prefixSum.get(sum));
            }
            else{
                prefixSum.put(sum,i);
            }
        }
        return ans;
    }
}
