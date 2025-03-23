class Solution {
    public int countWays(String digits) {
        int dp[]=new int[digits.length()+1];
        Arrays.fill(dp,-1);
       return find(0,digits,dp);
    }
    int find(int i,String str,int dp[]){
        if(i>=str.length()){
            return 1;
        }
        if(str.charAt(i)-'0'==0){
            return 0;
        }
        if(dp[i]!=-1){
            return dp[i];
        }
        int c1=find(i+1,str,dp);
        int c2=0;
        if(i+1<str.length()){
            int num=Integer.parseInt(str.substring(i,i+2));
            if(num<=26&&num>=10){
              c2=  find(i+2,str,dp);
            }
        }
        return dp[i]= c1+c2;
    }
    
}
