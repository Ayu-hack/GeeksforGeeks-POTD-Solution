class Solution {
    public int findMaxSum(int arr[]) {
        int n = arr.length;

        if (n == 0) return 0;
        if (n == 1) return arr[0];

        // Set previous 2 values
        int secondLast = 0, last = arr[0];

        // Compute current value using previous
        // two values. The final current value
        // would be our result
        int res = 0;
        for (int i = 1; i < n; i++) {
            res = Math.max(arr[i] + secondLast, last);
            secondLast = last;
            last = res;
        }

        return res;
    }
}
