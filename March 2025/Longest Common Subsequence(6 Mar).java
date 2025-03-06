class Solution {
    static int lcs(String s1, String s2) {
        // code here
        char c1[]=s1.toCharArray();
        char c2[]=s2.toCharArray();
        int m = s1.length();
        int n= s2.length();
        int memo[][]=new int[m+1] [n+1];
        for(int []row:memo)
        Arrays.fill(row,-1);
        int res= subseq(c1,c2,m,n,memo);
        return res;
    }
    static int subseq(char s1[],char s2[],int m ,int n , int memo[][])
    {
        if(m==0||n==0)
        return memo[m][n]=0;
        if(memo[m][n]!=-1)
        return memo[m][n];
        if(s1[m-1]==s2[n-1])
        memo[m][n]=1+subseq(s1,s2,m-1,n-1,memo);
        else
        memo[m][n]=Math.max(subseq(s1,s2,m,n-1,memo),subseq(s1,s2,m-1,n,memo));
        return memo[m][n];
    }
}
