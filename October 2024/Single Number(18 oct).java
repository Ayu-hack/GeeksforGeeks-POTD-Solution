// JAVA CODE

class Solution {
    int getSingle(int arr[]) {
        // code here
        int ans = 0;
        for(int x:arr)ans^=x;
        return ans;
    }

}
