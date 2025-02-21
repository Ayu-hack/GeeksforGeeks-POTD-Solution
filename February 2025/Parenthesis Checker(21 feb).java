class Solution {
    static boolean isBalanced(String s) {
        // code here
        Stack<Character> st = new Stack();
        for(char ch : s.toCharArray()){
            if(st.isEmpty() || ch == '(' || ch == '{' || ch == '['){
                st.push(ch);
            }
            else if((ch == ')' && st.peek() == '(') ||
            (ch == ']' && st.peek() == '[') || (ch == '}' && st.peek() == '{')){
                st.pop();
            }
            else {
                return false;
            }
        }
        return st.isEmpty();
    }
}
