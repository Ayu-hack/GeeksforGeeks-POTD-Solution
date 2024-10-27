class Solution {
    public boolean findTriplet(int[] arr) {
        int n = arr.length;
        if(n<3)return false;
        Arrays.sort(arr);
        for(int i=n-1;i>=2;i--){
            int j=i-1,k=0;
            while(k<j){
                int sum = arr[k]+arr[j];
                if(sum==arr[i])return true;
                else if(sum<arr[i])k++;
                else j--;
            }
        }
        return false;

        
    }
}
