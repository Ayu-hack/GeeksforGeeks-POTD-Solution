// JAVA CODE

class Solution {
     int totalCount(int k, int[] arr) {
        // code here
        int ans = 0;
        for(int x : arr) {
            ans += (x + k - 1) / k;
        }
        return ans;
    }

}
