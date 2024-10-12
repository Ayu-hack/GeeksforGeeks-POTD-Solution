class Solution {
    public int pairWithMaxSum(int[] arr) {
        
        // code here
        if (arr.length < 2) {
            return -1;
        }
        
        int sum = Integer.MIN_VALUE;
        int i = 1, j = arr.length;
        
        while (i < j) {
           sum = Math.max(arr[i] + arr[i-1], sum);
           i ++;
           
       }
       return sum;
    }
}
