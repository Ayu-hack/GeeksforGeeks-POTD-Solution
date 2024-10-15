//Array Pair Sum Divisibility Problem
//Given an array of integers nums and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.
//approach: The approach involves calculating the remainders of the array elements when divided by 𝑘k, counting their occurrences, and ensuring that each remainder can form valid pairs with its complementary remainder, with special checks for remainders 00 and 𝑘/2k/2.
//1st January
bool canArrange(vector<int>& nums, int k) {
    vector<int> remainderCount(k, 0);

    for (int num : nums) {
        int remainder = ((num % k) + k) % k;
        remainderCount[remainder]++;
    }

    if (remainderCount[0] % 2 != 0) return false;

    for (int i = 1; i <= k / 2; ++i) {
        if (i == k - i) {
            if (remainderCount[i] % 2 != 0) return false;
        } else {
            if (remainderCount[i] != remainderCount[k - i]) {
                return false;
            }
        }
    }

    return true;
}
