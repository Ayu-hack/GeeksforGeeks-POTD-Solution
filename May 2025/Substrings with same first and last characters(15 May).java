class Solution {
    public int countSubstring(String s) {
       int n=s.length();
       int count=0;
       HashMap<Character,Integer>ans=new HashMap<>();
       for(int i=0;i<n;i++){
           char ch=s.charAt(i);
           ans.put(ch,ans.getOrDefault(ch,0)+1);
           count+=ans.get(ch);
       }
        return count;
    }
}
