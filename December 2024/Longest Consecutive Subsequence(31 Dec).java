class Solution {

    // Function to return length of longest subsequence of consecutive integers.
    public int longestConsecutive(int[] arr) {
        // code here
        int ans=1;
        HashMap<Integer,Integer> mm = new HashMap<>();
        for(int x:arr){
            if(mm.get(x)==null){
                int left = mm.getOrDefault(x-1,0);
                int right = mm.getOrDefault(x+1,0);
                int total = left+right+1;
                mm.put(x,total);
                mm.put(x-left,total);
                mm.put(x+right,total);
                ans=Math.max(ans,total);
            }
        }
        return ans;
    }
}
