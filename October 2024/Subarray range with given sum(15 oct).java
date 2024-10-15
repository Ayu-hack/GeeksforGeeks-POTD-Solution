class Solution {
    // Function to count the number of subarrays which adds to the given sum.
    static int subArraySum(int arr[], int tar) {
        // add your code here
        Map<Integer,Integer> mm = new HashMap<>();
        int ans=0,sum=0;
        for(int x:arr){
            sum+=x;
            if(sum==tar)ans++;
            if(mm.get(sum-tar)!=null)ans+=mm.get(sum-tar);
            mm.put(sum,mm.getOrDefault(sum,0)+1);
        }
        return ans;
    }
}
