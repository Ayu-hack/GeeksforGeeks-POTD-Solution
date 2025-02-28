class Solution {
    public int evaluate(String[] arr) {
        // code here
        Stack<Integer> stack = new Stack();
        for(String ch: arr){
            if(isOperator(ch)){
                int b = stack.pop();
                int a = stack.pop();
                int res = apply(a, b, ch);
                stack.push(res);
            }
            else {
                stack.push(Integer.parseInt(ch));
            }
        }
        return stack.pop();
    }
    boolean isOperator(String s){
        return s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/");
    }
    int apply(int a, int b, String operator){
        switch(operator){
            case "+": return a+b;
            case "-": return a-b;
            case "*": return a*b;
            case "/": return a/b;
            default: return a;
        }
    }
}
