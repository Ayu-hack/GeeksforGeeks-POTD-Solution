// JAVA CODE

class Solution {
    // Returns count buildings that can see sunlight
    public int countBuildings(int[] height) {
        // code here
        int ans = 1, mx = height[0];
        for(int x:height){
            if(x>mx){
                mx=x;
                ans++;
            }
        }
        return ans;
    }

}
