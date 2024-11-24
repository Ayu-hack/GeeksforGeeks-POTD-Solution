class Solution {

    // arr: input array
    // Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(int[] arr) {

        // Your code here
        int sum=0,ans=Integer.MIN_VALUE,n=arr.length;
        for(int i=0;i<n;i++){
            sum+=arr[i];
            ans=Math.max(ans,sum);
            if(sum<0)sum=0;
        }
        return ans;
    }
}
