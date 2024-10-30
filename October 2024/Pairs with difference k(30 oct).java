class Solution {
    int countPairsWithDiffK(int[] arr, int k) {
        // code here
        int ans = 0;
        Map<Integer,Integer> mm = new HashMap<>();
        for(int x:arr)mm.put(x,mm.getOrDefault(x,0)+1);
        for(int x:arr)ans+=mm.getOrDefault(x+k,0);
        return ans;
    }

}
