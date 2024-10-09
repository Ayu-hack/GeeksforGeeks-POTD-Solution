class Solution {
    // Function to sort an array of 0s, 1s, and 2s
    public void sort012(int[] nums) {
        // code here
        int zero = 0, one = 0, two = 0, index = 0;

        for (int x : nums) {
            if (x == 0) zero ++;
            if (x == 1) one ++;
            if (x == 2) two ++;
        }

        for (int i = 0; i < nums.length; i++) {
            while (zero -- > 0) nums[index ++] = 0;
            while (one -- > 0)  nums[index ++] = 1;
            while (two -- > 0)  nums[index ++] = 2;
        }
    }
}
