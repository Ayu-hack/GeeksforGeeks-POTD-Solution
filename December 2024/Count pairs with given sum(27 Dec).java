class Solution {

     int countPairs(int arr[], int target) {
        // Your code here
        int ans=0;
        HashMap<Integer,Integer> mm = new HashMap<>();
        for(int x:arr){
            if(mm.get(target-x)!=null)ans+=mm.get(target-x);
            mm.put(x,mm.getOrDefault(x,0)+1);
        }
        return ans;
    }
}
