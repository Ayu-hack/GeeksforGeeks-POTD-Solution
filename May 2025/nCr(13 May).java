class Solution {
    public int nCr(int n, int r) {
        // Edge case where r is greater than n
        if (r > n) {
            return 0;
        }

        long sum = 1;

        // Calculate the value using
        // the binomial coefficient formula
        for (int i = 1; i <= r; i++) {
            sum = sum * (n - r + i) / i;
        }
        return (int)sum;
    }
}
