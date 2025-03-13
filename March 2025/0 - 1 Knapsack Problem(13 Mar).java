class Solution {
    static int solve(int capacity,int[] val,int[] wt,int index,int[][] dp){
        if(index==0){
            if(wt[0]<=capacity){
                return val[0];
            }else{
                return 0;
            }
        }
        if(dp[index][capacity] != -1){
            return dp[index][capacity];
        }
        int include = 0;
        if(wt[index]<=capacity){
            include = val[index]+solve(capacity-wt[index],val,wt,index-1,dp);
        }
        int exclude = solve(capacity,val,wt,index-1,dp);
        return dp[index][capacity] = Math.max(include,exclude);
    }
    
    static int knapsack(int W, int val[], int wt[]) {
        int[][] dp = new int[val.length][W+1];
        for(int i=0;i<val.length;i++){
            for(int j=0;j<W+1;j++){
                dp[i][j]=-1;
            }
        }
        return solve(W,val,wt,val.length-1,dp);
        
    }
}
