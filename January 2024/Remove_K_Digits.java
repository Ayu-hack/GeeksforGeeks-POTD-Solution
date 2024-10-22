import java.util.Stack;

class Solution {
    public String removeKdigits(String S, int K) {
        int n = S.length();
        Stack<Character> st = new Stack<Character>();
        for(int i=0; i<n; i++){
            while(!st.isEmpty() && K>0 && st.peek()-'0'>S.charAt(i)-'0'){
                st.pop();
                K=K-1;
            }
            st.push(S.charAt(i));
        }
        while(K>0){
            st.pop();
            K--;
        }
        if(st.isEmpty()) return "0";
        StringBuilder res = new StringBuilder();
        while(!st.isEmpty()){
            res.append(st.pop());
        }
        res.reverse();
        while (res.length()>1 && res.charAt(0)=='0') {
            res.deleteCharAt(0);
        }
        return res.length()==0 ? "0" : res.toString();
    }
}