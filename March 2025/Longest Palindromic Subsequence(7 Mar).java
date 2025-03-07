class Solution {
    int dp[][];
    public int f1(String s, String t, int i, int j){
        if(i<0 || j<0)return 0;
        if(s.charAt(i) == t.charAt(j)){
            return dp[i][j] = 1+f1(s, t, i-1, j-1);
        }
        
        if(dp[i][j] != -1)return dp[i][j];
        
        int first = f1(s, t, i-1, j);
        int second = f1(s, t, i, j-1);
        return dp[i][j] = Math.max(first, second);
    }
    
    public int longestPalinSubseq(String s) {
        // code here
        int n = s.length();
        dp = new int[n][n];
        for(int ar[]: dp){
            Arrays.fill(ar, -1);
        }
        StringBuilder sb = new StringBuilder(s);
        String r = sb.reverse().toString();
        return f1(s, r, n-1, n-1);
    }
}
