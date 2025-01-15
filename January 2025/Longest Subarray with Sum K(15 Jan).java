class Solution {
    public int longestSubarray(int[] arr, int k) {
        // code here
        HashMap<Integer,Integer> prefixSum = new HashMap<>();
        int n=arr.length,sum=0,ans=0;
        for(int i=0;i<n;i++){
            sum+=arr[i];
            if(sum==k){
                ans=i+1;
            }
            else if(prefixSum.get(sum-k)!=null){
                ans=Math.max(ans,i-prefixSum.get(sum-k));
            }
            if(prefixSum.get(sum)==null){
                prefixSum.put(sum,i);
            }
        }
        return ans;
    }

}
