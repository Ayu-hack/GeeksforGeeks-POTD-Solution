class Solution {
    Stack<Integer> st;
    Stack<Integer> minSt;
    
    public Solution() {
        st = new Stack<>();
        minSt = new Stack<>();
    }

    // Add an element to the top of Stack
    public void push(int x) {
        // code here
        st.push(x);
        
        if(minSt.isEmpty() || minSt.peek() >= x)
        minSt.push(x);
    }

    // Remove the top element from the Stack
    public void pop() {
        // code here
        if(st.isEmpty())
        return;
        
        int x = st.pop();
        
        if(minSt.peek() == x)
        minSt.pop();
    }

    // Returns top element of the Stack
    public int peek() {
        // code here
        if(st.isEmpty())
        return -1;
        
        return st.peek();
    }

    // Finds minimum element of Stack
    public int getMin() {
        // code here
        if(minSt.isEmpty())
        return -1;
        
        return minSt.peek();
    }
}
