class Solution {
    public int startStation(int[] gas, int[] cost) {
        // Your code here
        int n = gas.length;
        
        int sum = 0;
        int start = 0;
        for(int i=0; i<2*n; i++){
            int ind = i%n;
            sum+=(gas[ind]-cost[ind]);
            if(sum<0){
                sum = 0;
                start = i+1;
            }
            if(i-start==n){
                return start;
            }
        }
        return -1;
    }
}
