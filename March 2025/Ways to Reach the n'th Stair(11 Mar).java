class Solution {
    int countWays(int n) {
        // base case
        if (n <= 1) return 1;
        int a = 1, b = 1, temp;

        for (int i = 2; i <= n; i++) {
            temp = (a + b);
            a = b;
            b = temp;
        }
        return b;
    }
}
