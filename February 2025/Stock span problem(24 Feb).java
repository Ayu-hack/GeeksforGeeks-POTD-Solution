class Solution {
    public ArrayList<Integer> calculateSpan(int[] arr) {
        int n = arr.length;
        Stack<Integer> s = new Stack<>();
        s.push(0);
        ArrayList<Integer> S = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            S.add(0);
        }
        S.set(0, 1);

        for (int i = 1; i < n; i++) {
            while (!s.isEmpty() && arr[s.peek()] <= arr[i]) {
                s.pop();
            }
            int span = s.isEmpty() ? (i + 1) : (i - s.peek());
            S.set(i, span);
            s.push(i);
        }
        return S;
    }
}
