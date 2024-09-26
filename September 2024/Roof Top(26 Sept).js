// JAVA CODE


class Solution {
    // Function to find maximum number of consecutive steps
    // to gain an increase in altitude with each step.
    public int maxStep(int arr[]) {
        // Your code here
        int ans = 0,increaseCount = 0;
        for(int i=1;i<arr.length;i++){
            if(arr[i]>arr[i-1])increaseCount++;
            else{
                ans=Math.max(ans,increaseCount);
                increaseCount=0;
            }
        }
        ans=Math.max(ans,increaseCount);
        return ans;
    }

}
