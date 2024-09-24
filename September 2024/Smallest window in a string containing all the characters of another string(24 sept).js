// JAVA CODE



    class Solution
{
    //Function to find the smallest window in the string s consisting
    //of all the characters of string p.
    public static String smallestWindow(String s, String p)
    {
        // Your code here
        if(p.length()>s.length())return "-1";
        int forS[] = new int[26];
        int forP[] = new int[26];
        int c=0,c2=0,n=s.length(),m=p.length(),j=0,start=-1,end=-1,len=Integer.MAX_VALUE;
        for(int i=0;i<m;i++){
            char x = p.charAt(i);
            forP[x-'a']++;
            if(forP[x-'a']==1)c++;
        }
        for(int i=0;i<n;i++){
            char x = s.charAt(i);
            forS[x-'a']++;
            if(forS[x-'a']==forP[x-'a'])c2++;
            if(c2==c){
                while(forS[s.charAt(j)-'a']>forP[s.charAt(j)-'a'])forS[s.charAt(j++)-'a']--;
                if(len>i-j+1){
                    start=j;
                    end=i;
                    len=i-j+1;
                }
            }
        }
        if(start==-1)return "-1";
        return s.substring(start,end+1);
    }

}
