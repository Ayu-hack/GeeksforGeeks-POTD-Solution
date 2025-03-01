class Solution {
    static String decodeString(String s) {
        Stack<Character> st = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            // Push characters into the stack until ']' is encountered
            if (s.charAt(i) != ']') {
                st.push(s.charAt(i));
            }
            else {
                StringBuilder temp = new StringBuilder();
                while (!st.isEmpty() && st.peek() != '[') {
                    temp.insert(0, st.pop());
                }
                st.pop();

                StringBuilder num = new StringBuilder();
                while (!st.isEmpty() && Character.isDigit(st.peek())) {
                    num.insert(0, st.pop());
                }
                int number = Integer.parseInt(num.toString());
                StringBuilder repeat = new StringBuilder();
                for (int j = 0; j < number; j++) repeat.append(temp);
                for (char c : repeat.toString().toCharArray()) st.push(c);
            }
        }

        StringBuilder res = new StringBuilder();
        while (!st.isEmpty()) {
            res.insert(0, st.pop());
        }
        return res.toString();
    }
}
