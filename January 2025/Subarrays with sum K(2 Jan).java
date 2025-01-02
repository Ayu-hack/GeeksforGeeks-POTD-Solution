class Solution {
    public int countSubarrays(int arr[], int k) {
        // code here
        int sum=0,ans=0;
        HashMap<Integer,Integer> mm = new HashMap<>();
        for(int x:arr){
            sum+=x;
            if(sum==k)ans++;
            ans+=mm.getOrDefault(sum-k,0);
            mm.put(sum,mm.getOrDefault(sum,0)+1);
        }
        return ans;
    }
}
