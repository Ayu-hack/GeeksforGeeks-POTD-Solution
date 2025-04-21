class Solution {
    int missingNum(int arr[]) {
        // code here
        int n=arr.length+1;
        long sum=(long) n*(n+1)/2;
        for(long num:arr){
            sum-=num;
        }
        return (int) sum;
    }
}
